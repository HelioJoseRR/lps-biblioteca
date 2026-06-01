import os
import shutil
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = "output"
TEMPLATES_DIR = "templates"

def read_template(category, name):
    path = os.path.join(TEMPLATES_DIR, category, name)
    if not os.path.exists(path):
        path = os.path.join(TEMPLATES_DIR, "geral", name)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

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
    tmpl = read_template("geral", "docker-compose.yml.tmpl")
    content = tmpl.format(services_yml=services_yml)
    write_file(os.path.join(project_dir, "docker-compose.yml"), content)

def create_frontend(project_dir, features):
    frontend_dir = os.path.join(project_dir, "frontend")
    
    # Root files
    write_file(os.path.join(frontend_dir, "package.json"), read_template("frontend", "package.json.tmpl"))
    write_file(os.path.join(frontend_dir, "vite.config.js"), read_template("frontend", "vite.config.js.tmpl"))
    write_file(os.path.join(frontend_dir, "index.html"), read_template("frontend", "index.html.tmpl"))
    write_file(os.path.join(frontend_dir, "Dockerfile"), read_template("frontend", "Dockerfile.tmpl"))
    
    # src files
    write_file(os.path.join(frontend_dir, "src", "main.jsx"), read_template("frontend", "src/main.jsx.tmpl"))
    write_file(os.path.join(frontend_dir, "src", "App.jsx"), read_template("frontend", "src/App.jsx.tmpl"))
    write_file(os.path.join(frontend_dir, "src", "App.css"), read_template("frontend", "src/App.css.tmpl"))

def create_microservices(project_dir, features):
    for feat in features:
        feat_dir = os.path.join(project_dir, feat)
        
        # Dockerfile
        docker_tmpl = read_template("geral", "Dockerfile.python.tmpl")
        write_file(os.path.join(feat_dir, "Dockerfile"), docker_tmpl.format(port=8000))
        
        if feat == 'auth-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npython-jose[cryptography]\npasslib[bcrypt]\npython-multipart\n")
            main_py = read_template("auth-service", "main.py.tmpl")
        elif feat == 'catalogo-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npsycopg2-binary\n")
            main_py = read_template("catalogo-service", "main.py.tmpl")
        else:
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\n")
            main_tmpl = read_template("geral", "microservice_main.py.tmpl")
            main_py = main_tmpl.format(name=feat.capitalize(), id=feat)
            
        write_file(os.path.join(feat_dir, "main.py"), main_py)

def create_api_gateway(project_dir, features):
    gw_dir = os.path.join(project_dir, "api-gateway")
    docker_tmpl = read_template("geral", "Dockerfile.python.tmpl")
    write_file(os.path.join(gw_dir, "Dockerfile"), docker_tmpl.format(port=8080))
    write_file(os.path.join(gw_dir, "requirements.txt"), "fastapi\nuvicorn\nhttpx\n")
    
    routes = "\n".join([
        f"""
@app.api_route("/{feat}/{{path:path}}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_{feat.replace('-', '_')}(path: str):
    import httpx
    async with httpx.AsyncClient() as client:
        # Simplificacao: roteia para o container via docker network
        url = f"http://{feat}:8000/{{path}}"
        # No mundo real, repassariamos params e headers
        return {{"gateway": "Proxy to {feat}", "url": url}}
""" for feat in features])

    gw_tmpl = read_template("api-gateway", "main.py.tmpl")
    main_py = gw_tmpl.format(routes=routes, services_json=json.dumps(features))
    write_file(os.path.join(gw_dir, "main.py"), main_py)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    project_name = data.get('projectName', 'app')
    features = data.get('features', [])
    
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
        
        auth_sql = ""
        if 'auth-service' in features:
            auth_sql = """CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE, password_hash TEXT);
CREATE TABLE roles (id SERIAL PRIMARY KEY, name VARCHAR(20) UNIQUE);
INSERT INTO roles (name) VALUES ('admin'), ('user');"""

        services_sql = """CREATE TABLE IF NOT EXISTS livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano INTEGER,
    categoria VARCHAR(100)
);
INSERT INTO livros (titulo, autor, ano, categoria) VALUES 
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia'),
('1984', 'George Orwell', 1949, 'Distopia');"""

        sql_tmpl = read_template("geral", "init.sql.tmpl")
        sql_script = sql_tmpl.format(auth_sql=auth_sql, services_sql=services_sql)
        write_file(os.path.join(db_dir, "init.sql"), sql_script)

    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500
        
    return jsonify({"message": f"Aplicação '{project_name}' gerada com sucesso", "status": "success"}), 200

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
