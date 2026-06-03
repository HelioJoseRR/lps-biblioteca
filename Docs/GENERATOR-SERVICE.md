# ⚙️ Generator Service — Documentação

## Visão Geral

O **Generator Service** é o backend da LPS Biblioteca. Ele recebe uma lista de features selecionadas pelo usuário (via Selector UI) e gera uma aplicação completa e funcional composta por **microsserviços**, um **API Gateway**, um **frontend React**, um **banco de dados PostgreSQL**, e a orquestração via **Docker Compose**.

O serviço é uma API Flask que recebe a configuração desejada e, por meio de **templates**, compõe dinamicamente o código de cada módulo selecionado.

---

## 🛠️ Stack Tecnológica

| Tecnologia        | Versão     | Finalidade                                   |
|--------------------|------------|----------------------------------------------|
| **Python**         | 3.11       | Linguagem do gerador                         |
| **Flask**          | —          | Servidor HTTP (API REST)                     |
| **Flask-CORS**     | —          | Habilitar CORS para o frontend               |
| **Jinja2**         | —          | Dependência (disponível, não usada via engine)|
| **Docker**         | Python 3.11| Containerização                              |

---

## 📁 Estrutura de Arquivos

```
generator-service/
├── Dockerfile              # Container Python 3.11
├── generator.py            # Lógica principal do gerador
├── requirements.txt        # Dependências (flask, flask-cors, jinja2)
├── output/                 # Diretório de saída dos projetos gerados
└── templates/              # Templates de código para geração
    ├── .gitkeep
    ├── api-gateway/        # Template do API Gateway
    │   └── main.py.tmpl
    ├── auth-service/       # Template do Serviço de Autenticação
    │   └── main.py.tmpl
    ├── avaliacao-service/  # Template do Serviço de Avaliação
    │   └── main.py.tmpl
    ├── busca-service/      # Template do Serviço de Busca
    │   └── main.py.tmpl
    ├── catalogo-service/   # Template do Serviço de Catálogo
    │   └── main.py.tmpl
    ├── emprestimo-service/ # Template do Serviço de Empréstimo
    │   └── main.py.tmpl
    ├── multa-service/      # Template do Serviço de Multas
    │   └── main.py.tmpl
    ├── notificacao-service/# Template do Serviço de Notificação
    │   └── main.py.tmpl
    ├── frontend/           # Templates do Frontend React gerado
    │   ├── Dockerfile.tmpl
    │   ├── index.html.tmpl
    │   ├── package.json.tmpl
    │   ├── vite.config.js.tmpl
    │   └── src/
    │       ├── components/
    │       │   └── Estatisticas.jsx.tmpl
    │       ├── App.css.tmpl
    │       ├── App.jsx.tmpl
    │       └── main.jsx.tmpl
    └── geral/              # Templates compartilhados/genéricos
        ├── docker-compose.yml.tmpl
        ├── Dockerfile.nginx.tmpl
        ├── Dockerfile.python.tmpl
        ├── init.sql.tmpl
        └── microservice_main.py.tmpl
```

---

## 🔌 API

### `POST /generate`

Endpoint principal que recebe a configuração e gera o projeto.

**Request:**
```json
{
  "projectName": "minha-biblioteca",
  "features": ["catalogo-service", "auth-service", "emprestimo-service"]
}
```

**Response (sucesso — 200):**
```json
{
  "message": "Aplicação 'minha-biblioteca' gerada com sucesso",
  "status": "success"
}
```

**Response (erro — 500):**
```json
{
  "error": "Descrição do erro",
  "status": "error"
}
```

---

## 🧩 Módulos Gerados (por Feature)

A geração é orquestrada pela função `generate()`, que invoca quatro etapas em sequência:

1. `create_microservices()` — Gera os microsserviços selecionados
2. `create_api_gateway()` — Gera o API Gateway
3. `create_frontend()` — Gera o frontend React
4. `create_docker_compose()` — Gera o docker-compose.yml
5. **Schema SQL** — Gera o script de inicialização do banco de dados

---

### 📦 Módulo 1: Catálogo Service (`catalogo-service`)

**Categoria:** Core (obrigatório)

O serviço de catálogo gerencia o acervo de livros da biblioteca com persistência em PostgreSQL.

**Template:** `templates/catalogo-service/main.py.tmpl`
**Framework:** FastAPI + psycopg2

#### Features implementadas:

| Endpoint                | Método | Descrição                                      |
|-------------------------|--------|-------------------------------------------------|
| `GET /livros`           | GET    | Lista todos os livros (com busca opcional)       |
| `GET /livros/{id}`      | GET    | Obtém detalhes de um livro específico            |
| `GET /autores`          | GET    | Autocomplete de autores (min. 3 caracteres)      |
| `POST /livros`          | POST   | Adiciona novo livro (com upload de capa)         |

- **Upload de capas**: Suporte a upload de imagem de capa via `multipart/form-data`, salvo em `/uploads/`
- **Busca**: Filtro por título ou autor via query param `busca`
- **Modelo de dados**: `id`, `titulo`, `autor`, `ano`, `categoria`, `sinopse`, `tipo_edicao`, `capa_url`

---

### 📦 Módulo 2: Auth Service (`auth-service`)

**Categoria:** Segurança (opcional)

O serviço de autenticação gerencia login, registro, permissões, coleções pessoais e favoritos.

**Template:** `templates/auth-service/main.py.tmpl`
**Framework:** FastAPI + python-jose (JWT) + passlib (bcrypt) + psycopg2

#### Sub-módulo: Autenticação & Usuários

| Endpoint               | Método | Autenticação | Descrição                                  |
|------------------------|--------|:------------:|--------------------------------------------|
| `POST /auth/register`  | POST   | ❌            | Registra um novo usuário                   |
| `POST /auth/login`     | POST   | ❌            | Login com email/username + senha → JWT     |
| `GET /users/me`        | GET    | ✅ User       | Retorna dados do usuário logado            |

- **JWT**: Token com expiração de 60 min, contendo `sub` (ID), `username`, `role`
- **Migração de senha**: Suporta migração transparente de senhas em texto puro para bcrypt no primeiro login
- **OAuth2**: Compatível com OAuth2PasswordBearer

#### Sub-módulo: Painel Admin

| Endpoint                    | Método | Autenticação | Descrição                        |
|-----------------------------|--------|:------------:|----------------------------------|
| `GET /users`                | GET    | ✅ Admin      | Lista todos os usuários          |
| `PUT /users/{id}/role`      | PUT    | ✅ Admin      | Altera role de um usuário        |
| `DELETE /users/{id}`        | DELETE | ✅ Admin      | Exclui um usuário                |

- **Proteção**: Impede admin de excluir a si mesmo
- **Roles**: `admin` e `user`

#### Sub-módulo: Coleções

| Endpoint                                          | Método | Autenticação | Descrição                                   |
|---------------------------------------------------|--------|:------------:|---------------------------------------------|
| `POST /collections`                               | POST   | ✅ User       | Cria uma nova coleção                        |
| `GET /collections/me`                             | GET    | ✅ User       | Lista coleções do usuário logado             |
| `GET /collections`                                | GET    | ✅ User       | Lista coleções públicas de todos os usuários |
| `POST /collections/{id}/books/{book_id}`          | POST   | ✅ User       | Adiciona livro a uma coleção                 |
| `DELETE /collections/{id}/books/{book_id}`         | DELETE | ✅ User       | Remove livro de uma coleção                  |

- **Visibilidade**: Coleções podem ser públicas ou privadas (`is_public`)
- **Relacionamento**: Tabela auxiliar `collection_books` (N:N)

#### Sub-módulo: Favoritos

| Endpoint                  | Método | Autenticação | Descrição                              |
|---------------------------|--------|:------------:|----------------------------------------|
| `POST /favorites/{book_id}` | POST   | ✅ User       | Toggle favorito (adiciona ou remove)   |
| `GET /favorites`           | GET    | ✅ User       | Lista IDs dos livros favoritos         |

---

### 📦 Módulo 3: Empréstimo Service (`emprestimo-service`)

**Categoria:** Operacional (opcional)
**Dependências:** `auth-service`, `catalogo-service`

O serviço de empréstimo controla a retirada e devolução de livros, com limite de 1 empréstimo simultâneo por usuário.

**Template:** `templates/emprestimo-service/main.py.tmpl`
**Framework:** FastAPI + python-jose (JWT) + psycopg2

#### Features implementadas:

| Endpoint              | Método | Autenticação | Descrição                                        |
|-----------------------|--------|:------------:|--------------------------------------------------|
| `GET /status`         | GET    | ❌            | Lista IDs de livros emprestados (público)        |
| `GET /me`             | GET    | ✅ User       | Retorna o empréstimo atual do usuário             |
| `POST /{book_id}`     | POST   | ✅ User       | Realiza empréstimo de um livro                   |
| `DELETE /{book_id}`   | DELETE | ✅ User       | Devolve um livro (usuário ou admin)              |
| `GET /all`            | GET    | ✅ Admin      | Lista todos os empréstimos (painel admin)        |

- **Limite**: 1 empréstimo por usuário (constraint UNIQUE no `user_id`)
- **Exclusividade**: 1 empréstimo por livro (constraint UNIQUE no `book_id`)
- **Admin**: Admin pode devolver qualquer livro; o endpoint `/all` retorna dados completos com JOIN em `users` e `livros`

---

### 📦 Novos Módulos Integrados

Todos os módulos opcionais abaixo agora possuem templates dedicados e completos (não usam mais stubs genéricos):

- **Multa Service (`multa-service`)**: Gerencia punições por atrasos (status pendente/paga) com endpoint financeiro de resumo.
- **Notificação Service (`notificacao-service`)**: Roteia alertas broadcast ou diretos para usuários (lidas/não lidas).
- **Busca Service (`busca-service`)**: Oferece pesquisa com filtros avançados e consolida dados de estatísticas de todo o acervo.
- **Avaliação Service (`avaliacao-service`)**: Gerencia resenhas e reviews de usuários com notas (1-5 estrelas) e compila os top mais bem avaliados.

---

### 📦 API Gateway (`api-gateway`)

**Gerado sempre** (não é opcional)

O API Gateway funciona como ponto central de acesso para todos os microsserviços, roteando requisições com base no path.

**Template:** `templates/api-gateway/main.py.tmpl`
**Framework:** FastAPI + httpx (cliente HTTP assíncrono)

#### Features implementadas:

| Endpoint                      | Método   | Descrição                                     |
|-------------------------------|----------|-----------------------------------------------|
| `GET /`                      | GET      | Status do gateway + lista de serviços          |
| `ANY /{service}/{path}`      | Todos    | Proxy reverso para o microsserviço             |

- **Proxy reverso**: Encaminha `method`, `body`, `headers` e `query params`
- **Service discovery**: Baseado em nomes Docker (`http://{service}:8000`)
- **Erro 503**: Retornado quando o serviço alvo está indisponível
- **Erro 404**: Retornado quando o serviço não existe
- **Timeout**: 30 segundos
- **CORS**: Habilitado para todas as origens

---

### 📦 Módulo 5: Frontend React (gerado)

**Gerado sempre** (não é opcional)

Frontend React gerado dinamicamente com as features habilitadas.

**Templates:** `templates/frontend/`

#### Arquivos gerados:

| Arquivo                   | Descrição                                    |
|---------------------------|----------------------------------------------|
| `package.json`            | Dependências React + Vite                    |
| `vite.config.js`          | Configuração do bundler                      |
| `index.html`              | HTML raiz                                    |
| `Dockerfile`              | Container Nginx para produção                |
| `src/main.jsx`            | Entry point com ErrorBoundary                |
| `src/App.jsx`             | Componente principal (72KB de lógica)         |
| `src/App.css`             | Estilização completa (33KB)                  |
| `src/features.js`         | Array dinâmico das features habilitadas       |

- **ErrorBoundary**: Previne tela branca em caso de erro de renderização
- **Features dinâmicas**: O arquivo `features.js` é gerado com `enabledFeatures = [...]` baseado na seleção

---

### 📦 Módulo 6: Database (Schema SQL)

**Gerado sempre**

Script SQL de inicialização do PostgreSQL 15, gerado condicionalmente.

#### Tabelas geradas:

| Tabela              | Condição                           | Descrição                        |
|---------------------|-------------------------------------|----------------------------------|
| `roles`             | `auth-service` selecionado         | Papéis (admin, user)             |
| `users`             | `auth-service` selecionado         | Usuários com hash de senha       |
| `collections`       | `auth-service` selecionado         | Coleções pessoais de livros      |
| `collection_books`  | `auth-service` selecionado         | Relação N:N coleção ↔ livro     |
| `favorites`         | `auth-service` selecionado         | Livros favoritos por usuário     |
| `livros`            | Sempre                             | Catálogo de livros               |
| `emprestimos`       | `emprestimo-service` selecionado   | Empréstimos ativos               |

- **Seed data**: Dois livros de exemplo ("O Senhor dos Anéis", "1984") e um usuário admin padrão
- **Relações**: Foreign keys com `ON DELETE CASCADE`

---

### 📦 Módulo 7: Templates Gerais (`geral/`)

Templates compartilhados usados por múltiplos módulos:

| Template                     | Descrição                                        |
|------------------------------|--------------------------------------------------|
| `docker-compose.yml.tmpl`    | Orquestração completa (db, gateway, frontend + serviços) |
| `Dockerfile.python.tmpl`     | Dockerfile genérico para microsserviços Python   |
| `Dockerfile.nginx.tmpl`      | Dockerfile para servir frontend em Nginx          |
| `init.sql.tmpl`              | Wrapper do schema SQL                            |
| `microservice_main.py.tmpl`  | API FastAPI stub para features sem template específico |

---

### 📦 Módulos sem Template Específico

Não existem mais módulos gerados usando o template genérico (stub). Todos os módulos da arquitetura (Catálogo, Auth, Empréstimo, Multas, Notificação, Busca e Avaliação) possuem implementação de regras de negócios avançadas via seus templates próprios. O template genérico `geral/microservice_main.py.tmpl` permanece apenas como recurso (fallback) para eventuais novas features futuras.

---

## 🐳 Docker & Infraestrutura

O `generator-service` roda em um container Python 3.11 na porta `5000`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "generator.py"]
```

O projeto gerado cria sua própria stack Docker Compose com:
- **PostgreSQL 15** (porta 5432) — com init.sql montado
- **API Gateway** (porta 8080) — ponto de entrada centralizado
- **Frontend** (porta 3000) — servido via Nginx
- **Microsserviços** (portas 8000+) — cada um em seu container

---

## 🔄 Fluxo de Geração

```
1. Recebe POST /generate com projectName + features[]
2. Limpa diretório de saída anterior (se existir)
3. Para cada feature → gera microsserviço (Dockerfile, requirements, main.py)
4. Gera API Gateway com lista de serviços disponíveis
5. Gera Frontend React com features habilitadas
6. Gera docker-compose.yml unificando todos os serviços
7. Gera schema SQL condicional (auth tables + service tables)
8. Retorna mensagem de sucesso
```
