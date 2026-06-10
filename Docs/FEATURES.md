# Biblioteca LPS

**Descrição:** Linha de Produto de Software (LPS) para geração de backends de uma Biblioteca Online baseada em microsserviços. O projeto permite a seleção de features através de uma interface web, gerando dinamicamente uma aplicação backend customizada e pronta para uso.

---

## Tecnologias Utilizadas

O ecossistema é dividido em duas frentes principais de arquitetura:

*   **Selector UI (Frontend):** React, Next.js, Node.js.
*   **Generator Service (Backend Motor):** Python, Flask, Flask-CORS, Jinja2.

---

## Módulos Disponíveis para Geração

A aplicação gerada é composta por uma malha de microsserviços. Abaixo constam todos os módulos que podem ser incluídos na arquitetura, suas características e dependências:

### 1. Catálogo Service (Core)
O módulo núcleo e independente da biblioteca.
*   **Dependências:** Nenhuma (Sempre presente).
*   **Features Adicionadas:** Gestão do acervo (CRUD completo), validação inteligente contra duplicidade, metadados e performance garantida com paginação em listagens.
*   **Tecnologias Adicionadas:** Microsserviço em Node.js com Express e banco de dados PostgreSQL exclusivo.

### 2. Auth Service
Módulo de segurança e gerenciamento do perfil de usuário.
*   **Dependências:** Opcional (Nenhuma).
*   **Features Adicionadas:** Autenticação central, gestão de perfil de usuário (nome, e-mail, senha), criação de coleções personalizadas, marcação de favoritos e painel administrativo para elevação de permissões.
*   **Tecnologias Adicionadas:** Microsserviço em Node.js com Express e banco de dados PostgreSQL exclusivo.

### 3. Empréstimo Service
Módulo operacional responsável pela locação dos itens.
*   **Dependências:** Requer o *Auth Service* e o *Catálogo Service*.
*   **Features Adicionadas:** Fluxos de check-in e check-out de livros, motor de cálculos de prazos automatizados, auditoria de histórico de leituras e rastreio estratégico de inadimplência (atrasos).
*   **Tecnologias Adicionadas:** Microsserviço em Node.js com Express e banco de dados PostgreSQL exclusivo.

### 4. Busca Service
Módulo de exploração tática de leitura avançada do catálogo.
*   **Dependências:** Requer o *Catálogo Service*.
*   **Features Adicionadas:** Busca avançada com filtros compostos (título, autor, categoria, etc.), painéis dinâmicos de estatísticas do acervo e exibição rápida em destaques.
*   **Tecnologias Adicionadas:** Microsserviço em Node.js com Express e banco de dados PostgreSQL exclusivo.

### 5. Avaliação Service
Módulo social focado no engajamento de opiniões dos leitores.
*   **Dependências:** Requer o *Auth Service* e o *Catálogo Service*.
*   **Features Adicionadas:** Sistema de reviews (estrelas e resenhas), UPSERT nativo (para sobrescrita de nota), visibilidade cruzada de usuários e geração de ranking inteligente dos melhores do ano.
*   **Tecnologias Adicionadas:** Microsserviço em Node.js com Express e banco de dados PostgreSQL exclusivo.

### 6. Multa Service
Módulo financeiro de penalidade do ecossistema.
*   **Dependências:** Requer o *Empréstimo Service*.
*   **Features Adicionadas:** Atribuição manual de multas para avarias e atrasos excessivos, painel de quitação e resumo contábil sobre arrecadação da biblioteca.
*   **Tecnologias Adicionadas:** Microsserviço em Node.js com Express e banco de dados PostgreSQL exclusivo.

### 7. Notificação Service
Módulo de comunicação assíncrona entre o sistema e os leitores.
*   **Dependências:** Requer o *Auth Service*.
*   **Features Adicionadas:** Alertas e comunicações personalizadas, envio de mensagens em massa (broadcast), gestão unificada da caixa de entrada com contagem de notificações (badges) e ações em lote (ex: marcar todas como lidas).
*   **Tecnologias Adicionadas:** Microsserviço em Node.js com Express e banco de dados PostgreSQL exclusivo.

---

## Como Rodar o Projeto

Siga os passos abaixo de forma rápida para subir a solução localmente. É necessário ter `Git`, `Node.js 20+`, `Python 3.11+` e `Docker Desktop` instalados.

### 1. Clonagem do Repositório
```powershell
git clone <URL_DO_REPOSITORIO>
cd .\lps-biblioteca
```

### 2. Executar o Selector UI
```powershell
cd .\selector-ui
npm install
npm run dev
```
Acesse a URL padrão exibida no terminal.

### 3. Executar o Generator Service
Em outro terminal:
```powershell
cd .\generator-service
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python generator.py
```
O serviço estará aguardando requisições em `POST /generate`.

### 4. Executar a Aplicação Gerada
Após configurar na interface UI e gerar o projeto:
```powershell
cd .\generator-service\output\<uuid_gerado>
docker compose up -d
```
O gateway exporá a malha de APIs e bancos de dados automaticamente através do contêiner configurado.
