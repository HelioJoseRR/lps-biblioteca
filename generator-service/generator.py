import os
import shutil
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = "output"

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_docker_compose(project_dir, features):
    services_yml = ""
    for idx, feat in enumerate(features):
        port = 8000 + idx
        services_yml += f"""
  {feat}:
    build: ./{feat}
    ports:
      - "{port}:8000"
    environment:
      - DB_HOST=db
      - DB_USER=postgres
      - DB_PASS=postgres
    depends_on:
      - db
"""
    
    docker_compose_content = f"""version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: library_db
    ports:
      - "5432:5432"
    volumes:
      - ./database/init.sql:/docker-entrypoint-initdb.d/init.sql

  gateway:
    build: ./api-gateway
    ports:
      - "8080:8080"
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:80"
    depends_on:
      - gateway

{services_yml}
"""
    write_file(os.path.join(project_dir, "docker-compose.yml"), docker_compose_content)

def create_frontend(project_dir, features):
    frontend_dir = os.path.join(project_dir, "frontend")
    write_file(os.path.join(frontend_dir, "Dockerfile"), """FROM nginx:alpine
COPY ./src /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
""")
    
    features_list = "<ul>" + "".join([f"<li>{feat}</li>" for feat in features]) + "</ul>"
    
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Application</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f9fafb; color: #111827; }}
        h1 {{ color: #2563eb; }}
        .card {{ background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); margin-top: 20px; }}
        .docs-link {{ display: inline-block; margin-top: 15px; padding: 10px 15px; background: #2563eb; color: white; text-decoration: none; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>Application Dashboard</h1>
    <p>This frontend was dynamically generated based on your selections.</p>
    
    <div class="card">
        <h2>Provisioned Microservices:</h2>
        {features_list}
        
        <a href="http://localhost:8080/docs" target="_blank" class="docs-link">View API Gateway Documentation</a>
    </div>

    <script>
        fetch('http://localhost:8080/')
            .then(res => res.json())
            .then(data => console.log("Gateway Status:", data))
            .catch(err => console.error("Gateway is not reachable", err));
    </script>
</body>
</html>
"""
    write_file(os.path.join(frontend_dir, "src", "index.html"), index_html)

def create_microservices(project_dir, features):
    for feat in features:
        feat_dir = os.path.join(project_dir, feat)
        
        write_file(os.path.join(feat_dir, "Dockerfile"), """FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
""")
        
        write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\n")
        
        main_py = f"""from fastapi import FastAPI

app = FastAPI(title="{feat.capitalize()} API")

@app.get("/")
def read_root():
    return {{"service": "{feat}", "status": "running"}}

@app.get("/health")
def health_check():
    return {{"status": "ok"}}
"""
        write_file(os.path.join(feat_dir, "main.py"), main_py)

def create_api_gateway(project_dir, features):
    gw_dir = os.path.join(project_dir, "api-gateway")
    
    write_file(os.path.join(gw_dir, "Dockerfile"), """FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
""")
    
    write_file(os.path.join(gw_dir, "requirements.txt"), "fastapi\nuvicorn\nhttpx\n")
    
    routes = "\n".join([
        f"""
@app.get("/{feat}/{{path:path}}")
async def proxy_{feat.replace('-', '_')}(path: str):
    # Simulates proxy routing to the microservice
    return {{"gateway": "proxying to {feat}", "path": path}}
""" for feat in features])

    main_py = f"""from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI(title="API Gateway", description="Central routing for microservices. Interactive documentation available.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

{routes}

@app.get("/")
def root():
    return {{"status": "Gateway Operational", "services": {json.dumps(features)}}}

@app.get("/docs-redirect")
def redirect_docs():
    return RedirectResponse(url="/docs")
"""
    write_file(os.path.join(gw_dir, "main.py"), main_py)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    project_name = data.get('projectName', 'app')
    features = data.get('features', [])
    
    print(f"Gerando aplicação '{{project_name}}' com features: {{features}}")
    
    project_dir = os.path.join(OUTPUT_DIR, project_name)
    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)
    os.makedirs(project_dir, exist_ok=True)
    
    try:
        create_microservices(project_dir, features)
        create_api_gateway(project_dir, features)
        create_frontend(project_dir, features)
        create_docker_compose(project_dir, features)
        
        # Database schema
        db_dir = os.path.join(project_dir, "database")
        os.makedirs(db_dir, exist_ok=True)
        sql_script = "-- Auto-generated Database Schema\\n\\n"
        for feat in features:
            table_name = feat.replace('-', '_')
            sql_script += f"CREATE TABLE IF NOT EXISTS {table_name}_records (id SERIAL PRIMARY KEY, data JSONB);\\n"
        
        write_file(os.path.join(db_dir, "init.sql"), sql_script)

    except Exception as e:
        print(f"Erro ao gerar: {{e}}")
        return jsonify({{"error": str(e), "status": "error"}}), 500
        
    return jsonify({{"message": f"Aplicação '{{project_name}}' gerada com sucesso", "status": "success"}}), 200

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
