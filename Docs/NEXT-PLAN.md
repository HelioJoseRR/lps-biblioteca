# Plano de Migração para Next.js

Como desenvolvedor de software sênior, elaborei este plano de migração para transformar sua aplicação atual (React + Vite) em uma aplicação Next.js. 

O foco deste plano é ser **incremental e seguro**. Faremos a migração passo a passo para que, a cada etapa, a aplicação continue funcionando, preservando todas as features atuais de forma isolada.

## 🎯 Objetivo
Migrar o projeto `selector-ui` (atualmente usando Vite) para Next.js (utilizando o App Router moderno), sem reescrever a lógica de negócio ou quebrar o que já está construído.

---

## 🛠️ Fase 1: Preparação e Instalação de Dependências
*O objetivo desta fase é colocar o Next.js no projeto junto com o Vite, preparando o terreno sem deletar nada ainda.*

- [x] **1. Instalar o Next.js:** 
  Rodar o comando `npm install next` no diretório `selector-ui`.
- [x] **2. Atualizar o `package.json`:** 
  Modificar a seção de `scripts` para incluir os comandos do Next.js sem remover os do Vite imediatamente (podemos chamá-los de `next-dev`, `next-build`, etc., para fins de transição).
- [x] **3. Criar a configuração do Next.js:** 
  Adicionar um arquivo `next.config.mjs` (ou `.js`) básico na raiz de `selector-ui`.

---

## 🏗️ Fase 2: Estruturação Base (App Router)
*Aqui vamos criar a casca do Next.js que vai engolir a sua aplicação React atual.*

- [x] **1. Criar o diretório de rotas:**
  Criar a pasta `app` dentro de `src/` (ficando `src/app`). O Next.js suporta a pasta `src` nativamente.
- [x] **2. Criar o `layout.jsx` global:**
  Dentro de `src/app`, criar um arquivo `layout.jsx`. Ele substituirá o papel do seu arquivo `index.html` antigo, contendo as tags `<html>` e `<body>`.
- [x] **3. Migrar os estilos globais:**
  Importar o `index.css` e `App.css` para dentro do novo `layout.jsx`.

---

## 🧩 Fase 3: Acoplamento do App Atual (Estratégia "Use Client")
*A chave para não perder as features já feitas é trazer o seu `App.jsx` inteiro como um componente Client-Side dentro da página inicial do Next.js.*

- [x] **1. Criar a página principal (`page.jsx`):**
  Criar o arquivo `src/app/page.jsx`.
- [x] **2. Importar o `App.jsx`:**
  Dentro de `page.jsx`, importar o componente principal `App` que já existe (`src/App.jsx`).
- [x] **3. Adicionar `"use client"`:**
  Como o Vite é um SPA renderizado no cliente, o `App.jsx` provavelmente usa `useState`, `useEffect` ou eventos de clique. Vamos adicionar a diretiva `"use client"` no topo do `App.jsx` (ou criar um wrapper) para que o Next.js saiba que ele deve ser renderizado no navegador, mantendo seu comportamento idêntico ao original.

---

## 🖼️ Fase 4: Ajustes de Arquivos Estáticos (Assets)
*Garantir que imagens e fontes continuem carregando perfeitamente.*

- [x] **1. Migrar a pasta pública:**
  Certificar-se de que qualquer arquivo servido na raiz do Vite (na pasta `public/`) seja mantido. O Next.js também usa uma pasta `public` com comportamento semelhante.
- [x] **2. Caminhos de importação:**
  Validar se os arquivos em `src/assets/` estão sendo carregados corretamente no build do Next.js.

---

## 🧹 Fase 5: Limpeza e Remoção do Vite
*Apenas quando a aplicação estiver rodando perfeitamente pelo Next.js (em `localhost:3000`), faremos a limpeza final.*

- [x] **1. Atualizar Scripts Definitivos:**
  Renomear os scripts de Next.js no `package.json` para serem os padrões (`dev`, `build`, `start`).
- [x] **2. Desinstalar o Vite:**
  Rodar `npm uninstall vite @vitejs/plugin-react`.
- [x] **3. Remover Arquivos Residuais:**
  Deletar os arquivos exclusivos do Vite que não são mais necessários: `vite.config.js`, `index.html` da raiz, e o arquivo de entrada `src/main.jsx`.

---

## 🚀 Próximos Passos (Evolução Futura)
Uma vez que o projeto estiver seguro e rodando no Next.js, as próximas melhorias (opcionais) podem incluir:
- Separar o "monolito" `App.jsx` em múltiplas páginas baseadas em pastas dentro de `src/app`.
- Aproveitar o **Server-Side Rendering (SSR)** para partes da aplicação que não dependem de estado do usuário, melhorando o SEO e a performance inicial.
- Trocar tags `<img>` pelo componente otimizado `<Image>` do `next/image`.
- Migrar chamadas de API feitas no cliente para *Server Components* ou *Server Actions*.

***

> **Nota do Arquiteto:** 
> Se desejar prosseguir, basta aprovar este plano. Posso iniciar a execução da Fase 1 e 2 imediatamente e irmos validando passo a passo.

---

# Parte 2: Migração dos Templates do Gerador (Aplicações Geradas)

Além do `selector-ui`, a aplicação gerada dinamicamente pelo sistema (através do `generator-service`) também deve ser construída em Next.js. O principal requisito arquitetural aqui é garantir a **idempotência das features**: a lógica que liga e desliga módulos conforme a escolha do usuário deve ser mantida intacta, sem vazamento de escopo.

## 🛠️ Fase 1: Atualização dos Arquivos de Configuração
*Preparar os templates básicos para um projeto Next.js em vez de Vite.*

- [x] **1. Atualizar `package.json.tmpl`:** 
  Substituir as dependências e scripts do Vite pelos do Next.js (scripts `dev`, `build`, `start`, dependência `next`).
- [x] **2. Remover Templates Obsoletos:** 
  Deletar `vite.config.js.tmpl` e `index.html.tmpl` do `generator-service/templates/frontend/`.
- [x] **3. Atualizar `Dockerfile.tmpl`:** 
  Modificar o Dockerfile do frontend gerado para expor a porta `3000` (padrão Next.js) e configurar o comando de inicialização correto (`npm run dev` com host `0.0.0.0`).

## 🏗️ Fase 2: Estruturação do App Router nos Templates
*Criar a base estrutural que o Next.js exige (`app/layout.jsx` e `app/page.jsx`).*

- [x] **1. Criar Template `layout.jsx.tmpl`:**
  Este arquivo servirá como o "esqueleto" HTML da aplicação gerada, importando os estilos globais (`index.css` e `App.css`) e contendo as tags fundamentais (`<html>`, `<body>`).
- [x] **2. Criar Template `page.jsx.tmpl`:**
  Este será o ponto de entrada principal que importará e renderizará o `<App />`.
- [x] **3. Remover Template `main.jsx.tmpl`:**
  O arquivo de entrada antigo do Vite não será mais necessário.

## 🧩 Fase 3: Preservação Funcional das Features (A Mágica do Isolamento)
*Garantir que a seleção de módulos no `selector-ui` reflita com precisão na aplicação final.*

- [x] **1. Manutenção do `features.js`:**
  O script `generator.py` continuará criando o arquivo `features.js` com o array `enabledFeatures`. Essa é a "fonte da verdade" injetada dinamicamente pelo gerador.
- [x] **2. Diretiva `"use client"` no `App.jsx.tmpl`:**
  O `App.jsx.tmpl` possui lógicas pesadas de estado (`useState`, `useEffect`) e verificações contínuas no array `enabledFeatures` (ex: `{enabledFeatures.includes('auth-service') && ...}`). Adicionaremos a diretiva `"use client"` no topo deste arquivo para que o Next.js o renderize no cliente (CSR). Isso assegura que **todas as condicionais de features continuarão operando exatamente como antes**, eliminando o risco de um módulo aparecer sem ter sido selecionado ou perder suas funcionalidades.

## ⚙️ Fase 4: Atualização do Engine do Gerador (`generator.py`)
*Modificar a lógica em Python para compor os novos arquivos.*

- [x] **1. Alterar caminhos de gravação:**
  O `generator.py` precisará gravar o `layout.jsx` e `page.jsx` na pasta `src/app/` em vez da raiz do `src/`.
- [x] **2. Adaptar limpeza e cópia:**
  Garantir que o script Python não tente mais gravar os arquivos antigos do Vite (como `index.html` e `vite.config.js`).

***

> **Nota do Arquiteto (Parte 2):**
> O plano garante segurança total: a lógica que decide qual módulo (auth, notificações, empréstimos, etc) será exibido está protegida pela importação estrita do array `enabledFeatures`. 
> 
> Você aprova esta arquitetura para as aplicações geradas? Se sim, me avise para eu começar as modificações nos templates em `generator-service`!
