# 📘 Selector UI — Documentação

## Visão Geral

O **Selector UI** é a interface gráfica do projeto **LPS Biblioteca** (Linha de Produto de Software). Ele permite que o usuário selecione quais **features/módulos** deseja incluir na aplicação de biblioteca que será gerada, configure o nome do projeto, e dispare a geração da aplicação através de uma chamada ao `generator-service`.

---

## 🛠️ Stack Tecnológica

| Tecnologia        | Versão     | Finalidade                          |
|--------------------|------------|-------------------------------------|
| **React**          | 19.x       | Biblioteca de UI (componentes)      |
| **Vite**           | 8.x        | Bundler e dev server                |
| **Vanilla CSS**    | —          | Estilização com tema dark premium   |
| **ESLint**         | 10.x       | Linting de código                   |
| **Docker**         | Node 20    | Containerização do dev server       |

---

## 📁 Estrutura de Arquivos

```
selector-ui/
├── Dockerfile              # Container Node 20 + Vite dev server
├── index.html              # HTML raiz com SEO, Google Fonts (Inter)
├── package.json            # Dependências e scripts
├── vite.config.js          # Configuração do Vite
├── public/                 # Assets estáticos
└── src/
    ├── main.jsx            # Ponto de entrada React (StrictMode)
    ├── App.jsx             # Componente principal da aplicação
    ├── App.css             # Estilização completa (dark theme premium)
    ├── features.js         # Definição das features selecionáveis
    ├── index.css            # Reset CSS base
    └── assets/             # Assets internos
```

---

## 🧩 Componentes Implementados

### `App.jsx` — Componente Principal

O componente `App` é o coração da interface, responsável por toda a lógica de seleção e geração. Ele está dividido em três regiões visuais:

#### 1. **Navbar** (Header)
- Título do projeto ("⚡ Biblioteca LPS")
- Badge com progresso (ex: "3 de 7 features")
- Input para definir o **nome do projeto** (padrão: `minha-biblioteca`)

#### 2. **Sidebar** (Painel Esquerdo — Categorias)
- Lista de categorias com ícones emoji
- Categorias extraídas dinamicamente do array de features
- Filtro "Todas" para exibir todas as features
- Contador de features selecionadas por categoria
- Categorias disponíveis: `Core`, `Segurança`, `Operacional`, `Financeiro`, `Comunicação`, `Exploração`, `Social`

#### 3. **Main Content** (Grade de Feature Cards)
- Cards interativos para cada feature
- Checkbox animado com ícone SVG de check
- Nome, descrição e categoria de cada feature
- Badges indicando "Obrigatória" ou "Opcional"
- Indicador de dependências com tooltip
- Animação de fade-in escalonada nos cards

#### 4. **Summary Panel** (Painel Direito — Resumo)
- Barra de progresso animada (com efeito shimmer)
- Lista das features selecionadas
- Botão principal "🚀 Gerar Aplicação"
- Botão "Resetar Seleção"
- Mensagens de sucesso/erro

---

## ⚙️ Lógica de Seleção de Features

### Gerenciamento de Dependências
A seleção implementa um sistema de **resolução transitiva de dependências**:

- **Ao selecionar** uma feature: todas as suas dependências são automaticamente selecionadas (de forma recursiva/transitiva).
- **Ao desselecionar** uma feature: todas as features que dependem dela são automaticamente desselecionadas (cascata reversa).

### Gerenciamento de Exclusões
- Features podem ter exclusões mútuas (`excludes`). Ao selecionar uma feature, features conflitantes são automaticamente removidas da seleção.

### Features Obrigatórias
- Features com `mandatory: true` estão sempre selecionadas e não podem ser desselecionadas pelo usuário.

---

## 📋 Catálogo de Features

| ID                     | Nome                       | Categoria     | Obrigatória | Dependências                          |
|------------------------|----------------------------|---------------|:-----------:|---------------------------------------|
| `catalogo-service`     | Serviço de Catálogo        | Core          | ✅           | —                                     |
| `auth-service`         | Serviço de Autenticação    | Segurança     | ❌           | —                                     |
| `emprestimo-service`   | Serviço de Empréstimo      | Operacional   | ❌           | `auth-service`, `catalogo-service`    |
| `multa-service`        | Serviço de Multas          | Financeiro    | ❌           | `emprestimo-service`                  |
| `notificacao-service`  | Serviço de Notificação     | Comunicação   | ❌           | `auth-service`                        |
| `busca-service`        | Serviço de Busca           | Exploração    | ❌           | `catalogo-service`                    |
| `avaliacao-service`    | Serviço de Avaliação       | Social        | ❌           | `auth-service`, `catalogo-service`    |

---

## 🌐 Comunicação com o Backend

A UI se comunica com o `generator-service` via requisição **HTTP POST**:

```
POST http://localhost:5000/generate
Content-Type: application/json

{
  "projectName": "minha-biblioteca",
  "features": ["catalogo-service", "auth-service", "emprestimo-service"]
}
```

- **Sucesso**: Mensagem verde indicando o path de saída (`output/<projectName>/`)
- **Erro**: Mensagem vermelha com detalhes do erro

---

## 🎨 Design & Estilização

O CSS implementa um **tema dark premium** com as seguintes características:

- **Paleta de cores**: Tons de indigo/violeta como accent (#6366f1, #818cf8), fundo escuro profundo (#06080f → #0a0e1a)
- **Glassmorphism**: Navbar com `backdrop-filter: blur(20px)` e borders translúcidas
- **Tipografia**: Google Font **Inter** com pesos variados (400–900)
- **Design tokens**: Variáveis CSS para cores, raios, transições e dimensões
- **Micro-animações**:
  - Fade-in escalonado nos cards (`cardFadeIn`)
  - Shimmer effect na barra de progresso
  - Hover com translate e box-shadow
  - Checkbox com scale transition
  - Botão primário com light sweep on hover
- **Layout responsivo**: Breakpoints em 1024px e 768px com reorganização em coluna
- **Max-width**: 1440px centrado para telas grandes

---

## 🐳 Docker

O `Dockerfile` utiliza `node:20-alpine` e expõe a porta `5173` para o dev server do Vite:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]
```

O serviço é orquestrado via `docker-compose.yml` na raiz do projeto, dependendo do `generator-service`.
