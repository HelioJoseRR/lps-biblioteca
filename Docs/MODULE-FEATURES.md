# 📋 Funcionalidades por Módulo (Microservices)

Este documento centraliza e descreve todas as funcionalidades, regras de negócio e operações (endpoints) incluídas em cada um dos módulos gerados pelo `generator-service` da LPS-Biblioteca.

---

## 🔐 1. Auth Service (Segurança e Perfis)
Responsável por toda a autenticação central, gestão de usuários, papéis (roles) e extensões de preferências bibliográficas.
* **Gestão de Perfil:** Atualização de dados pessoais (username/email) e alteração segura de senhas.
* **Coleções Personalizadas:** Permite a criação de pastas organizadoras públicas ou privadas de livros, onde o usuário insere ou remove itens livremente.
* **Favoritos:** Sistema rápido de marcação (like) de livros favoritos vinculados ao perfil.
* **Painel Administrativo:** Permite gerir as permissões e elevar usuários normais a `admin`.

## 📚 2. Catálogo Service (Core)
O coração da aplicação, focado no gerenciamento das obras físicas ou digitais disponíveis na biblioteca.
* **Gestão do Acervo (CRUD):** Permite aos administradores cadastrar, listar, atualizar e deletar livros (bloqueando a exclusão de itens que estejam em circulação ativa).
* **Validação Inteligente:** Bloqueia o registro de livros em duplicidade utilizando verificações mistas de título e autor.
* **Metadados:** Expõe dicionários e listagens puras das categorias, garantindo consistência aos selects do frontend.
* **Performance:** Todas as rotas de listagem contam com suporte nativo à paginação escalável.

## 🔄 3. Empréstimo Service (Operacional)
Controla a locação e a janela de temporalidade no qual as obras ficam sob posse do usuário.
* **Check-in / Check-out:** Registra transações de empréstimo e a baixa com soft-delete preenchendo a `data_devolucao`.
* **Motor de Prazos:** Define prazos limite automatizados no momento do empréstimo (ex: validade de 14 dias).
* **Auditoria de Histórico:** Usuários conseguem listar não apenas o que estão lendo, mas o que já leram no passado.
* **Rastreio de Inadimplência:** Endpoint estratégico para administradores varrerem rapidamente os empréstimos em atraso (livros não devolvidos dentro do prazo estipulado).

## 🔍 4. Busca Service (Exploração)
Separação tática do escopo de leitura avançada do Catálogo para um serviço especialista, evitando sobrecarga no módulo core.
* **Busca Composta (Filtros):** Executa query parameters combinados (título, autor, categoria e anos base).
* **Estatísticas Dinâmicas:** Exibe painéis resumidos do inventário (quantos livros há de ficção científica vs. literatura nacional, por exemplo).
* **Destaques:** Exposição rápida de vitrines de itens recém-adicionados.

## ⭐ 5. Avaliação Service (Social)
Módulo focado no engajamento da comunidade de leitores e democratização da opinião.
* **Sistema de Reviews:** Avaliação estrelada combinada a feedback textual (resenhas).
* **UPSERT Nativo:** Evita o acúmulo de notas repetidas pelo mesmo usuário em um único livro — permitindo a edição e sobreposição transparente do voto.
* **Visibilidade Cruzada:** Nas páginas das obras, expõe o que as pessoas estão achando da leitura, trazendo o respectivo identificador (`username`).
* **Ranking de Melhores do Ano (Top 10):** Realiza agregações complexas (`AVG` das notas e `COUNT` dos votos) para entregar as obras mais bem aceitas pelo público de forma instantânea.

## 💰 6. Multa Service (Financeiro)
Módulo disciplinar voltado à aplicação e quitação de penalidades por irregularidades de empréstimos.
* **Atribuição Manual de Multas:** O administrador pode gerar boletos/multas baseando-se no ID do usuário e justificando o motivo (avaria, perda ou atraso exorbitante).
* **Painel de Quitação:** Usuários podem visualizar suas dívidas (`pendente`) e sinalizar o pagamento para mudar de status (`paga`).
* **Resumo Contábil:** Fornece à diretoria a visão macro do total arrecadado pela biblioteca com punições vs. o dinheiro que ainda falta entrar.

## 🔔 7. Notificação Service (Comunicação)
Canal assíncrono interno da plataforma para notificar leitores sem a necessidade de envio de emails externos.
* **Alertas Personalizados:** Inserção de mensagens classificadas (infos cotidianas, alertas severos, confirmações de sucesso) destinadas a um perfil restrito.
* **Massa (Broadcast):** Sistema de megafone para administradores propagarem anúncios do sistema para toda a base.
* **Gestão da Caixa de Entrada:** Suporte de emblemas (`badges`) que indicam o número de notificações aguardando leitura.
* **Ações em Lote:** Limpeza de status marcando "todas como lidas".

## ⚙️ 8. Generator Service (Motor / Internals)
O sistema construtor que gerencia o ciclo de vida do projeto LPS.
* **Compilador Jinja2:** Substituição das macros por um ecossistema mais resiliente, robusto e flexível para renderizar dependências variadas (Python, React, YAML).
* **Exportação Prática (ZIP):** Capacidade de zippar nativamente todo o backend montado em tempo de execução para distribuição em ambientes Desktop/Cloud do cliente final.
* **Baterias Inclusas:** Auto-scaffolding inteligente injetando o `.env` de configuração local e um `README.md` contextualizado ao pacote arquitetural que o usuário requisitou.
