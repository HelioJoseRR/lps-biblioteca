# 📋 Backlog — Generator Service

> Backlog de tarefas para completar a implementação dos módulos do Generator Service.
> Cada módulo que hoje usa o template genérico (stub) precisa de um template dedicado com funcionalidades reais.

---

## 🔢 Prioridade

| Símbolo | Significado        |
|:-------:|:-------------------|
| 🔴      | Alta prioridade    |
| 🟡      | Média prioridade   |
| 🟢      | Baixa prioridade   |

---

## 📦 Módulo: Multa Service (`multa-service`)

> **Status atual:** Stub genérico (apenas `/` e `/health`)
> **Dependência:** `emprestimo-service`
> **Categoria:** Financeiro

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| M-1 | ✅         | Criar tabela `multas` no schema SQL                                                                   | Campos: `id`, `user_id`, `emprestimo_id`, `valor`, `motivo`, `status` (pendente/paga), `created_at`           |
| M-2 | ✅         | Criar template `templates/multa-service/main.py.tmpl`                                                 | API FastAPI com conexão ao PostgreSQL e autenticação JWT                                                      |
| M-3 | ✅         | Endpoint `GET /multas/me` — Listar multas do usuário                                                  | Retorna todas as multas do usuário logado, com status e valor                                                 |
| M-4 | ✅         | Endpoint `POST /multas` — Criar multa (admin)                                                         | Admin pode criar multa manualmente informando `user_id`, `valor` e `motivo`                                   |
| M-5 | ✅         | Endpoint `PUT /multas/{id}/pagar` — Marcar multa como paga                                            | O próprio usuário ou admin pode marcar uma multa como paga (muda status para "paga")                          |
| M-6 | ✅         | Endpoint `GET /multas/all` — Listar todas as multas (admin)                                           | Painel admin com todas as multas, incluindo dados do usuário (JOIN)                                           |
| M-7 | ✅         | Endpoint `GET /multas/resumo` — Resumo financeiro (admin)                                             | Retorna total de multas pendentes, total de multas pagas, e valor total arrecadado                            |
| M-8 | ✅         | Atualizar `generator.py` para incluir requirements e schema do multa-service                          | Adicionar `python-jose`, `psycopg2-binary` ao requirements e gerar tabela `multas` no init.sql                |

---

## 📦 Módulo: Notificação Service (`notificacao-service`)

> **Status atual:** Stub genérico (apenas `/` e `/health`)
> **Dependência:** `auth-service`
> **Categoria:** Comunicação

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| N-1 | ✅         | Criar tabela `notificacoes` no schema SQL                                                             | Campos: `id`, `user_id`, `titulo`, `mensagem`, `tipo` (info/alerta/sucesso), `lida` (bool), `created_at`      |
| N-2 | ✅         | Criar template `templates/notificacao-service/main.py.tmpl`                                           | API FastAPI com conexão ao PostgreSQL e autenticação JWT                                                      |
| N-3 | ✅         | Endpoint `GET /notificacoes/me` — Listar notificações do usuário                                      | Retorna todas as notificações do usuário logado, ordenadas por data (mais recente primeiro)                    |
| N-4 | ✅         | Endpoint `POST /notificacoes` — Enviar notificação (admin)                                            | Admin pode enviar notificação para um usuário específico informando `user_id`, `titulo`, `mensagem` e `tipo`  |
| N-5 | ✅         | Endpoint `POST /notificacoes/broadcast` — Enviar para todos (admin)                                   | Admin envia mesma notificação para todos os usuários cadastrados                                              |
| N-6 | ✅         | Endpoint `PUT /notificacoes/{id}/ler` — Marcar como lida                                              | O usuário marca uma notificação como lida                                                                     |
| N-7 | ✅         | Endpoint `PUT /notificacoes/ler-todas` — Marcar todas como lidas                                      | O usuário marca todas as suas notificações como lidas de uma vez                                              |
| N-8 | ✅         | Endpoint `GET /notificacoes/count` — Contador de não lidas                                            | Retorna a quantidade de notificações não lidas (para badge no frontend)                                       |
| N-9 | ✅         | Atualizar `generator.py` para incluir requirements e schema do notificacao-service                    | Adicionar dependências e gerar tabela `notificacoes` no init.sql                                              |

---

## 📦 Módulo: Busca Service (`busca-service`)

> **Status atual:** Stub genérico (apenas `/` e `/health`)
> **Dependência:** `catalogo-service`
> **Categoria:** Exploração

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| B-1 | ✅         | Criar template `templates/busca-service/main.py.tmpl`                                                 | API FastAPI com conexão ao PostgreSQL (sem autenticação — serviço público)                                    |
| B-2 | ✅         | Endpoint `GET /busca` — Busca avançada de livros                                                      | Busca por múltiplos campos (`titulo`, `autor`, `categoria`, `ano_min`, `ano_max`) via query params            |
| B-3 | ✅         | Endpoint `GET /busca/categorias` — Listar categorias disponíveis                                      | Retorna lista de categorias distintas existentes no catálogo (para filtros no frontend)                        |
| B-4 | ✅         | Endpoint `GET /busca/recentes` — Livros adicionados recentemente                                      | Retorna os últimos 10 livros adicionados ao catálogo (ordenados por ID decrescente)                           |
| B-5 | ✅         | Endpoint `GET /busca/estatisticas` — Estatísticas do acervo                                           | Retorna contagem total de livros, livros por categoria, e livros por tipo de edição                           |
| B-6 | ✅         | Suporte a paginação na busca                                                                           | Adicionar query params `page` e `per_page` ao endpoint de busca, com resposta incluindo `total` e `pages`     |
| B-7 | ✅         | Atualizar `generator.py` para incluir requirements do busca-service                                   | Adicionar `psycopg2-binary` ao requirements gerado                                                            |

---

## 📦 Módulo: Avaliação Service (`avaliacao-service`)

> **Status atual:** Stub genérico (apenas `/` e `/health`)
> **Dependência:** `auth-service`, `catalogo-service`
> **Categoria:** Social

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| A-1 | ✅         | Criar tabela `avaliacoes` no schema SQL                                                               | Campos: `id`, `user_id`, `book_id`, `nota` (1-5), `comentario` (text), `created_at`. UNIQUE(user_id, book_id) |
| A-2 | ✅         | Criar template `templates/avaliacao-service/main.py.tmpl`                                             | API FastAPI com conexão ao PostgreSQL e autenticação JWT                                                      |
| A-3 | ✅         | Endpoint `POST /avaliacoes/{book_id}` — Criar ou atualizar avaliação                                  | Usuário envia nota (1-5) e comentário. Se já avaliou, atualiza (UPSERT)                                      |
| A-4 | ✅         | Endpoint `GET /avaliacoes/{book_id}` — Listar avaliações de um livro                                  | Retorna todas as avaliações de um livro, com username do autor e data                                         |
| A-5 | ✅         | Endpoint `GET /avaliacoes/{book_id}/media` — Nota média de um livro                                   | Retorna a média aritmética das notas e a quantidade de avaliações                                             |
| A-6 | ✅         | Endpoint `GET /avaliacoes/me` — Minhas avaliações                                                     | Lista todas as avaliações feitas pelo usuário logado                                                          |
| A-7 | ✅         | Endpoint `DELETE /avaliacoes/{book_id}` — Remover avaliação                                           | Usuário pode remover sua própria avaliação; admin pode remover qualquer uma                                   |
| A-8 | ✅         | Endpoint `GET /avaliacoes/top` — Livros mais bem avaliados                                            | Retorna os 10 livros com maior média de notas (mínimo 1 avaliação)                                           |
| A-9 | ✅         | Atualizar `generator.py` para incluir requirements e schema do avaliacao-service                      | Adicionar dependências e gerar tabela `avaliacoes` no init.sql                                                |

---

## 📦 Módulo: Catálogo Service (`catalogo-service`) — Melhorias

> **Status atual:** Implementado com CRUD básico
> **Categoria:** Core

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| C-1 | ✅         | Endpoint `PUT /livros/{id}` — Editar livro                                                            | Atualizar dados de um livro existente (título, autor, ano, etc.)                                              |
| C-2 | ✅         | Endpoint `DELETE /livros/{id}` — Remover livro                                                        | Exclui um livro do catálogo (verificar se não está emprestado)                                                |
| C-3 | ✅         | Endpoint `GET /livros/categorias` — Listar categorias                                                 | Retorna categorias distintas para popular dropdowns no frontend                                               |
| C-4 | ✅         | Suporte a paginação em `GET /livros`                                                                  | Adicionar `page` e `per_page` com metadados de paginação na resposta                                         |
| C-5 | ✅         | Validação de duplicidade ao adicionar livro                                                           | Verificar se já existe livro com mesmo título + autor antes de inserir                                        |

---

## 📦 Módulo: Auth Service (`auth-service`) — Melhorias

> **Status atual:** Implementado com auth, admin, coleções e favoritos
> **Categoria:** Segurança

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| AU-1 | ✅        | Endpoint `PUT /users/me` — Editar perfil                                                              | Usuário pode atualizar seu próprio `username` e `email`                                                       |
| AU-2 | ✅        | Endpoint `PUT /users/me/password` — Alterar senha                                                     | Usuário informa senha atual + nova senha para alteração                                                       |
| AU-3 | ✅        | Endpoint `DELETE /collections/{id}` — Excluir coleção                                                 | Usuário pode excluir uma coleção própria                                                                      |
| AU-4 | ✅        | Endpoint `PUT /collections/{id}` — Editar coleção                                                     | Alterar nome, descrição ou visibilidade da coleção                                                            |

---

## 📦 Módulo: Empréstimo Service (`emprestimo-service`) — Melhorias

> **Status atual:** Implementado com CRUD de empréstimos
> **Categoria:** Operacional

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| E-1 | ✅         | Adicionar campo `data_devolucao` na tabela empréstimos                                                | Registrar quando o livro foi efetivamente devolvido (ao invés de deletar o registro)                          |
| E-2 | ✅         | Endpoint `GET /historico` — Histórico de empréstimos do usuário                                       | Retorna empréstimos atuais e passados do usuário logado                                                       |
| E-3 | ✅         | Adicionar campo `prazo_devolucao` (ex: 14 dias)                                                       | Calcular data limite de devolução ao criar empréstimo                                                         |
| E-4 | ✅         | Endpoint `GET /atrasados` — Listar empréstimos atrasados (admin)                                      | Retorna empréstimos cuja data limite já passou                                                                |

---

## 📦 Módulo: Generator Service — Melhorias Internas

> Melhorias na engine de geração em si.

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| G-1 | ✅         | Migrar templates de `str.format()` para Jinja2                                                        | Usar o motor de template Jinja2 (já é dependência) para templates mais legíveis e poderosos                   |
| G-2 | ✅         | Endpoint `GET /templates` — Listar templates disponíveis                                              | Retorna lista de features com template dedicado vs. genérico                                                  |
| G-3 | ✅         | Endpoint `GET /download/{project}` — Baixar projeto gerado como ZIP                                   | Compactar o diretório de saída e permitir download direto                                                     |
| G-4 | ✅         | Adicionar `.env.tmpl` ao projeto gerado                                                               | Gerar arquivo `.env` com variáveis de ambiente padrão (DB_HOST, JWT_SECRET, etc.)                             |
| G-5 | ✅         | Gerar `README.md` no projeto de saída                                                                 | README automático listando features habilitadas, portas, e como rodar                                         |

---

## 📦 Módulo: Frontend Gerado — Melhorias

> Melhorias nos templates do frontend React gerado.

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| F-1 | ✅         | Tela de Multas no frontend                                                                            | Componente para listar multas do usuário e botão de "marcar como paga"                                        |
| F-2 | ✅         | Tela de Notificações no frontend                                                                      | Componente com lista de notificações e badge de "não lidas" no header                                         |
| F-3 | ✅         | Tela de Avaliações no frontend                                                                        | Componente com estrelas (1-5) e campo de comentário em cada livro                                             |
| F-4 | ✅         | Filtros avançados na tela de catálogo                                                                  | Dropdowns de categoria, tipo de edição, e slider de ano para filtrar livros                                   |
| F-5 | ✅         | Tela de Estatísticas no frontend                                                                      | Dashboard com cards mostrando total de livros, empréstimos ativos, multas pendentes, etc.                     |

---

## 📊 Resumo do Backlog

| Módulo                | Novas Tasks | Status                  |
|-----------------------|:-----------:|-------------------------|
| Multa Service         | 8           | ✅ Concluído            |
| Notificação Service   | 9           | ✅ Concluído            |
| Busca Service         | 7           | ✅ Concluído            |
| Avaliação Service     | 9           | ✅ Concluído            |
| Catálogo (melhorias)  | 5           | ✅ Concluído            |
| Auth (melhorias)      | 4           | ✅ Concluído            |
| Empréstimo (melhorias)| 4           | ✅ Concluído            |
| Generator (melhorias) | 5           | ✅ Concluído            |
| Frontend (melhorias)  | 5           | ✅ Concluído            |
| Polimento UI/UX       | 9           | ✅ Concluído            |
| **Total**             | **65**      |                         |

---

## 🎨 Polimento UI/UX e Correções (Bugfixes)

> Conjunto de correções de bugs, persistência de estado e refatoração de interface (Nível Sênior).

### Tasks

| #   | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|-----|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| P-1 | ✅         | Correção de Bug F-1 (Multas)                                                                          | Corrigir leitura de atributos undefined (`total_pago`, `total_pendente`) no React, causador de tela em branco |
| P-2 | ✅         | Refatoração Página de Livro (F-3)                                                                     | Criar componente de estrelas (Stars), repaginar seção de avaliações e organizar action buttons lateralmente   |
| P-3 | ✅         | Refatoração Navbar Global                                                                             | Condensar navegação dos 7 módulos e menu de usuário utilizando ícones com tooltip, criando um layout mais clean |
| P-4 | ✅         | Dados complementares em Estatísticas (F-5)                                                            | Fazer Busca-Service retornar número de Usuários, Empréstimos e Avaliações do BD e popular o frontend          |
| P-5 | ✅         | Refatoração UI de Estatísticas (F-5)                                                                  | Renderizar as estatísticas em Cards Modernos com ícones SVG                                                   |
| P-6 | ✅         | Refatoração UI de Filtros Avançados (F-4)                                                             | Colocar os selects de Categoria e Ano em um bloco contíguo moderno na Landing Page                            |
| P-7 | ✅         | Correção da Barra de Busca na Home                                                                    | Ajustar `fetchLivros()` para enviar parâmetro correto (`q`) e corrigir Busca-Service para pesquisar Título ou Autor|
| P-8 | ✅         | Persistência de Sessão e Estado de View (F5)                                                          | Salvar `currentView` no `localStorage` para impedir que um refresh do browser devolva o usuário à página inicial |
| P-9 | ✅         | Formulário de Notificações (Painel Admin)                                                             | Re-implementar o envio de mensagens Broadcast ou Diretas pelo Admin no React                                  |

---

## 🚀 Fase 2: Polimento UI/UX e Estrutura (Routing)

> Nova iteração de melhorias focada em Routing, Sessões e um redesign moderno de componentes da interface.

### Tasks

| #    | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|------|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| F2-1 | ✅         | Implementar URL Routing (Hash)                                                                        | Substituir controle de `view` manual por `window.location.hash` (`#/landing`, `#/livro`), permitindo atalhos e Voltar/Avançar |
| F2-2 | ✅         | Substituir LocalStorage por SessionStorage                                                            | Garantir que dados sensíveis de Auth e Estado apaguem quando a aba/sessão for fechada, limpando o cache       |
| F2-3 | ✅         | Redesign Moderno da Navbar                                                                            | Utilizar botões estilo *Pill* interativos, e separar o Sino de Notificação isolado com Ponto Vermelho (Red Dot)|
| F2-4 | ✅         | Interatividade no Componente de Avaliação (Estrelas)                                                  | Corrigir problema das 5 estrelas engessadas usando estado de `hover` para preenchimento interativo em tempo real |
| F2-5 | ✅         | Redesign do Modal de Coleções                                                                         | Substituir o antigo "carousel de cards" num modal confuso por uma lista vertical limpa com caixas de seleção (Checkboxes) |
| F2-6 | ✅         | Autocomplete em Envios de Notificação (Admin)                                                         | Usar `<datalist>` no formulário de disparo para buscar e autocompletar nomes de usuários em vez de IDs numéricos secos |

---

## 🌟 Fase 3: Refinamento UI/UX Final

> Última rodada de ajustes estéticos, estruturais e de experiência de usuário, simulando padrões modernos (ex: YouTube, Componentização).

### Tasks

| #    | Prioridade | Task                                                                                                  | Descrição                                                                                                     |
|------|:----------:|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| F3-1 | ✅         | Extração do Componente `Estatisticas`                                                                 | Isolar o painel de métricas em `Estatisticas.jsx.tmpl` com layout moderno em CSS Grid e Banners Dark.         |
| F3-2 | ✅         | Bugfix: Sino de Notificação (Red Dot)                                                                 | Corrigir leitura da chave de resposta (`unread_count` vs `count`) integrando o backend com a UI.              |
| F3-3 | ✅         | Refatoração Navbar (Dropdown de Usuário)                                                              | Alterar o nome do usuário para um botão interativo (`user-pill-clickable`) com menu suspenso e clique fora.   |
| F3-4 | ✅         | Layout *YouTube Style* na Página de Detalhes                                                          | Remover barra lateral vertical. Alocar os botões na horizontal sob a sinopse e os comentários em *full width* |
| F3-5 | ✅         | Proteção Administrativa de Demissão                                                                   | Prevenir visualmente e logicamente que um `admin` rebaixe a si próprio caso seja o único admin existente.     |
| F3-6 | ✅         | Suporte SVG Color Dinâmico (`currentColor`)                                                           | Ajustar os ícones de estrela para herdar a cor nativa de feedback durante o *hover* de avaliação de obras.    |
