import graphviz

dot = graphviz.Digraph(comment='Dependências dos Microsserviços')
dot.attr(rankdir='TB', bgcolor='white')

features = {
    'catalogo': ('Catálogo\nService', '#22c55e'),
    'auth': ('Auth\nService', '#6366f1'),
    'emprestimo': ('Empréstimo\nService', '#6366f1'),
    'multa': ('Multa\nService', '#6366f1'),
    'notificacao': ('Notificação\nService', '#6366f1'),
    'busca': ('Busca\nService', '#6366f1'),
    'avaliacao': ('Avaliação\nService', '#6366f1'),
}

for fid, (label, color) in features.items():
    dot.node(fid, label, shape='box', style='filled', fillcolor=color, fontcolor='white')

dot.edge('auth', 'emprestimo', label='depende')
dot.edge('catalogo', 'emprestimo', label='depende')
dot.edge('emprestimo', 'multa', label='depende')
dot.edge('auth', 'notificacao', label='depende')
dot.edge('catalogo', 'busca', label='depende')
dot.edge('auth', 'avaliacao', label='depende')
dot.edge('catalogo', 'avaliacao', label='depende')

dot.render('Docs/img/dependencias_servicos', format='png', cleanup=True)
print('Grafo gerado: Docs/img/dependencias_servicos.png')
