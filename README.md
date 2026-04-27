# Biblioteca LPS

Linha de Produto de Software (LPS) para geração de backends de uma **Biblioteca Online** baseada em microsserviços. O projeto permite selecionar features em uma interface web e gerar, automaticamente, uma aplicação backend customizada no diretório `output\`.

## Informações

- **Nome do projeto:** Biblioteca LPS  
- **Autor:** Hélio José  
- **Disciplina:** Tópicos em Engenharia de Software: Projetando Linhas de Produto de Software  
- **Professor:** Arturo Hernandez Dominguez  
- **Instituição:** Instituto de Computação - UFAL  
- **Período:** 6º período

## Visão geral da solução

O projeto é dividido em dois blocos principais:

1. **Selector UI (React + Vite):** interface para seleção de features e configurações básicas da aplicação.
2. **Generator Service (Flask):** recebe o JSON da UI, processa templates com Jinja2, cria os microsserviços selecionados e monta o `docker-compose.yml` final.

Arquitetura final gerada:

- Microsserviços em **Node.js + Express**
- Banco de dados **PostgreSQL isolado por serviço**
- **API Gateway (Nginx)** para roteamento único de entrada
- Estrutura de saída por execução em `output\<uuid>\`

## Estrutura do diretório

```text
lps-biblioteca/
|-- .github/                          # Configurações de apoio ao repositório (instruções e automações)
|-- generator-service/                # Serviço gerador (Flask) da LPS
|   |-- templates/                    # Templates base dos microsserviços (Node/Express)
|   |-- output/                       # Saídas geradas por execução (organizadas por UUID)
|   |-- generator.py                  # Endpoint POST /generate e lógica de geração
|   |-- docker-compose.yml            # Compose base/final para execução da solução gerada
|   `-- requirements.txt              # Dependências Python do gerador
|-- selector-ui/                      # Frontend de seleção de features
|   |-- public/                       # Arquivos estáticos da interface
|   |-- src/                          # Código-fonte React
|   |-- package.json                  # Dependências e scripts npm
|   `-- vite.config.js                # Configuração do Vite
`-- .gitignore                        # Arquivos e pastas ignorados no versionamento
```

## Features e dependências da LPS

- `catalogo-service`: feature core (sempre presente)
- `auth-service`: opcional
- `emprestimo-service`: depende de `auth-service` e `catalogo-service`
- `multa-service`: depende de `emprestimo-service`
- `notificacao-service`: depende de `auth-service`
- `busca-service`: depende de `catalogo-service`
- `avaliacao-service`: depende de `auth-service` e `catalogo-service`

## Instalação de ferramentas

Instale previamente no ambiente:

- **Git**
- **Node.js 20+** (com npm)
- **Python 3.11+**
- **Docker Desktop** (Docker Engine + Docker Compose)

Verificação rápida (PowerShell):

```powershell
git --version
node -v
npm -v
python --version
docker --version
docker compose version
```

## Como rodar o projeto

### 1. Clonar e acessar o repositório

```powershell
git clone <URL_DO_REPOSITORIO>
cd .\lps-biblioteca
```

### 2. Subir o Selector UI (frontend)

```powershell
cd .\selector-ui
npm install
npm run dev
```

Após iniciar, acesse a URL exibida no terminal (padrão do Vite: `http://localhost:5173`).

### 3. Subir o Generator Service (backend Flask)

```powershell
cd .\generator-service
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python generator.py
```

Com o serviço em execução, a rota principal para geração é:

- `POST /generate`

### 4. Gerar e executar a aplicação customizada

Com as features selecionadas na UI e o JSON enviado para o gerador:

1. O backend cria uma pasta única em `output\<uuid>\`
2. Os serviços selecionados são materializados a partir dos templates
3. O `docker-compose.yml` final é montado automaticamente

Para executar a aplicação gerada:

```powershell
cd .\generator-service\output\<uuid>
docker compose up -d
```

Para parar:

```powershell
docker compose down
```

## Exemplo de payload para geração

```json
{
  "projectName": "biblioteca-online",
  "features": [
    "catalogo-service",
    "auth-service",
    "emprestimo-service",
    "multa-service",
    "notificacao-service"
  ]
}
```

## Resultado esperado

Ao final do fluxo, você terá uma aplicação backend de biblioteca online:

- Customizada pelas features selecionadas
- Pronta para subir com Docker Compose
- Estruturada em microsserviços com gateway e bancos isolados
