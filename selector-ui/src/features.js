export const features = [
  {
    id: 'catalogo-service',
    name: 'Serviço de Catálogo',
    category: 'Core',
    description: 'Gerenciamento de livros e acervo da biblioteca. (Core)',
    mandatory: true,
    dependencies: [],
    excludes: []
  },
  {
    id: 'auth-service',
    name: 'Serviço de Autenticação',
    category: 'Segurança',
    description: 'Login, registro e gestão de permissões de usuários.',
    mandatory: false,
    dependencies: [],
    excludes: []
  },
  {
    id: 'emprestimo-service',
    name: 'Serviço de Empréstimo',
    category: 'Operacional',
    description: 'Controle de empréstimos, devoluções e disponibilidade.',
    mandatory: false,
    dependencies: ['auth-service', 'catalogo-service'],
    excludes: []
  },
  {
    id: 'multa-service',
    name: 'Serviço de Multas',
    category: 'Financeiro',
    description: 'Cálculo e gestão de multas por atrasos na devolução.',
    mandatory: false,
    dependencies: ['emprestimo-service'],
    excludes: []
  },
  {
    id: 'notificacao-service',
    name: 'Serviço de Notificação',
    category: 'Comunicação',
    description: 'Envio de alertas e comunicações aos usuários.',
    mandatory: false,
    dependencies: ['auth-service'],
    excludes: []
  },
  {
    id: 'busca-service',
    name: 'Serviço de Busca',
    category: 'Exploração',
    description: 'Sistema de busca avançada e filtros de acervo.',
    mandatory: false,
    dependencies: ['catalogo-service'],
    excludes: []
  },
  {
    id: 'avaliacao-service',
    name: 'Serviço de Avaliação',
    category: 'Social',
    description: 'Avaliações e comentários de usuários sobre os livros.',
    mandatory: false,
    dependencies: ['auth-service', 'catalogo-service'],
    excludes: []
  }
];
