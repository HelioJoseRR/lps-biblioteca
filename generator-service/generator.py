import os
import shutil
import json
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from jinja2 import Template

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
    content = Template(tmpl).render(services_yml=services_yml)
    write_file(os.path.join(project_dir, "docker-compose.yml"), content)

def create_frontend(project_dir, features):
    frontend_dir = os.path.join(project_dir, "frontend")
    
    # Root files
    write_file(os.path.join(frontend_dir, "package.json"), read_template("frontend", "package.json.tmpl"))
    write_file(os.path.join(frontend_dir, "Dockerfile"), read_template("frontend", "Dockerfile.tmpl"))
    
    # src/app files
    write_file(os.path.join(frontend_dir, "src", "app", "layout.jsx"), read_template("frontend", "src/app/layout.jsx.tmpl"))
    write_file(os.path.join(frontend_dir, "src", "app", "page.jsx"), read_template("frontend", "src/app/page.jsx.tmpl"))
    
    # src files
    write_file(os.path.join(frontend_dir, "src", "App.jsx"), read_template("frontend", "src/App.jsx.tmpl"))
    write_file(os.path.join(frontend_dir, "src", "App.css"), read_template("frontend", "src/App.css.tmpl"))
    write_file(os.path.join(frontend_dir, "src", "features.js"), f"export const enabledFeatures = {json.dumps(features)};")
    
    # src/components
    write_file(os.path.join(frontend_dir, "src", "components", "Estatisticas.jsx"), read_template("frontend", "src/components/Estatisticas.jsx.tmpl"))

def create_microservices(project_dir, features):
    for feat in features:
        feat_dir = os.path.join(project_dir, feat)
        
        # Dockerfile
        docker_tmpl = read_template("geral", "Dockerfile.python.tmpl")
        write_file(os.path.join(feat_dir, "Dockerfile"), Template(docker_tmpl).render(port=8000))
        
        if feat == 'auth-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npython-jose[cryptography]\nbcrypt==3.2.2\npasslib[bcrypt]\npython-multipart\npsycopg2-binary\n")
            main_py = read_template("auth-service", "main.py.tmpl")
        elif feat == 'catalogo-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npsycopg2-binary\npython-multipart\n")
            main_py = read_template("catalogo-service", "main.py.tmpl")
        elif feat == 'emprestimo-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npython-jose[cryptography]\npsycopg2-binary\n")
            main_py = read_template("emprestimo-service", "main.py.tmpl")
        elif feat == 'busca-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npsycopg2-binary\n")
            main_py = read_template("busca-service", "main.py.tmpl")
        elif feat == 'multa-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npython-jose[cryptography]\npsycopg2-binary\n")
            main_py = read_template("multa-service", "main.py.tmpl")
        elif feat == 'avaliacao-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npython-jose[cryptography]\npsycopg2-binary\n")
            main_py = read_template("avaliacao-service", "main.py.tmpl")
        elif feat == 'notificacao-service':
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\npython-jose[cryptography]\npsycopg2-binary\n")
            main_py = read_template("notificacao-service", "main.py.tmpl")
        else:
            write_file(os.path.join(feat_dir, "requirements.txt"), "fastapi\nuvicorn\n")
            main_tmpl = read_template("geral", "microservice_main.py.tmpl")
            main_py = Template(main_tmpl).render(name=feat.capitalize(), id=feat)
            
        write_file(os.path.join(feat_dir, "main.py"), main_py)

def create_api_gateway(project_dir, features):
    gw_dir = os.path.join(project_dir, "api-gateway")
    docker_tmpl = read_template("geral", "Dockerfile.python.tmpl")
    write_file(os.path.join(gw_dir, "Dockerfile"), Template(docker_tmpl).render(port=8080))
    write_file(os.path.join(gw_dir, "requirements.txt"), "fastapi\nuvicorn\nhttpx\n")
    
    gw_tmpl = read_template("api-gateway", "main.py.tmpl")
    main_py = Template(gw_tmpl).render(services_json=json.dumps(features))
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
        
        # G-4: .env
        env_content = "DB_HOST=db\nDB_USER=postgres\nDB_PASS=postgres\nDB_NAME=library_db\n"
        write_file(os.path.join(project_dir, ".env"), env_content)
        
        # G-5: README.md
        readme_content = f"# Projeto {project_name}\n\n## Serviços Incluídos\n"
        for feat in features:
            readme_content += f"- {feat}\n"
        readme_content += "\n## Como executar\n`docker-compose up --build`\n"
        write_file(os.path.join(project_dir, "README.md"), readme_content)
        
        # Database schema
        db_dir = os.path.join(project_dir, "database")
        os.makedirs(db_dir, exist_ok=True)
        
        auth_sql = ""
        if 'auth-service' in features:
            auth_sql = """CREATE TABLE IF NOT EXISTS roles (id SERIAL PRIMARY KEY, name VARCHAR(20) UNIQUE);
INSERT INTO roles (name) VALUES ('admin'), ('user') ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) DEFAULT 'user'
);

-- Note: Senha inicial 'admin' em texto puro. O auth-service fará a migração para bcrypt no primeiro login.
INSERT INTO users (username, email, password_hash, role) 
SELECT 'Admin', 'admin@example.com', 'admin', 'admin' 
WHERE NOT EXISTS (SELECT 1 FROM users WHERE email = 'admin@example.com');

CREATE TABLE IF NOT EXISTS collections (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    is_public BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS collection_books (
    collection_id INTEGER REFERENCES collections(id) ON DELETE CASCADE,
    book_id INTEGER NOT NULL,
    PRIMARY KEY (collection_id, book_id)
);

CREATE TABLE IF NOT EXISTS favorites (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    book_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, book_id)
);"""

        services_sql = """CREATE TABLE IF NOT EXISTS livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano INTEGER,
    categoria VARCHAR(100),
    sinopse TEXT,
    tipo_edicao VARCHAR(50),
    capa_url VARCHAR(255)
);
INSERT INTO livros (titulo, autor, ano, categoria, sinopse, tipo_edicao) VALUES 
('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954, 'Fantasia', 'A grande jornada para destruir o Um Anel.', 'Capa Dura'),
('1984', 'George Orwell', 1949, 'Ficção Científica', 'Uma distopia onde o Grande Irmão tudo vê.', 'Bolso');"""

        if 'emprestimo-service' in features:
            services_sql += """
CREATE TABLE IF NOT EXISTS emprestimos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    book_id INTEGER NOT NULL REFERENCES livros(id) ON DELETE CASCADE,
    data_emprestimo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    prazo_devolucao TIMESTAMP,
    data_devolucao TIMESTAMP DEFAULT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_emprestimos_user_ativo ON emprestimos (user_id) WHERE data_devolucao IS NULL;
CREATE UNIQUE INDEX IF NOT EXISTS idx_emprestimos_book_ativo ON emprestimos (book_id) WHERE data_devolucao IS NULL;"""

        if 'multa-service' in features:
            services_sql += """
CREATE TABLE IF NOT EXISTS multas (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    emprestimo_id INTEGER NOT NULL REFERENCES emprestimos(id) ON DELETE CASCADE,
    valor NUMERIC(10, 2) NOT NULL,
    motivo VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'pendente',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

        if 'avaliacao-service' in features:
            services_sql += """
CREATE TABLE IF NOT EXISTS avaliacoes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    book_id INTEGER NOT NULL REFERENCES livros(id) ON DELETE CASCADE,
    nota INTEGER CHECK (nota >= 1 AND nota <= 5),
    comentario TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, book_id)
);"""

        if 'notificacao-service' in features:
            services_sql += """
CREATE TABLE IF NOT EXISTS notificacoes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    titulo VARCHAR(255) NOT NULL,
    mensagem TEXT NOT NULL,
    tipo VARCHAR(50) DEFAULT 'info',
    lida BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

        sql_tmpl = read_template("geral", "init.sql.tmpl")
        sql_script = Template(sql_tmpl).render(auth_sql=auth_sql, services_sql=services_sql)
        write_file(os.path.join(db_dir, "init.sql"), sql_script)

    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500
        
    return jsonify({"message": f"Aplicação '{project_name}' gerada com sucesso", "status": "success"}), 200

@app.route('/templates', methods=['GET'])
def list_templates():
    templates = {}
    for root, dirs, files in os.walk(TEMPLATES_DIR):
        if root == TEMPLATES_DIR: continue
        category = os.path.basename(root)
        templates[category] = [f for f in files if f.endswith('.tmpl')]
    return jsonify(templates)

@app.route('/download/<project>', methods=['GET'])
def download_project(project):
    project_dir = os.path.join(OUTPUT_DIR, project)
    if not os.path.exists(project_dir):
        return jsonify({"error": "Project not found"}), 404
        
    zip_path = os.path.join(OUTPUT_DIR, f"{project}")
    shutil.make_archive(zip_path, 'zip', project_dir)
    return send_file(f"{zip_path}.zip", as_attachment=True)

if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
