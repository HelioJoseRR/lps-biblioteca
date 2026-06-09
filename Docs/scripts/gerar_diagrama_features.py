import graphviz

dot = graphviz.Digraph(comment='FODA - Feature Diagram Biblioteca LPS')
dot.attr(rankdir='TB', bgcolor='white', splines='ortho')

# Nodes
dot.node('root', 'Biblioteca Online', shape='box', style='filled', fillcolor='#1e40af', fontcolor='white')

# Mandatory Features (filled circle on edge in FODA, here we use colors)
dot.node('catalogo', 'Catálogo\n(Mandatory)', shape='box', style='filled', fillcolor='#16a34a', fontcolor='white')

# Optional Features
dot.node('auth', 'Autenticação\n(Optional)', shape='box', style='filled', fillcolor='#f59e0b', fontcolor='white')
dot.node('emprestimo', 'Empréstimo\n(Optional)', shape='box', style='filled', fillcolor='#f59e0b', fontcolor='white')
dot.node('multa', 'Multa\n(Optional)', shape='box', style='filled', fillcolor='#f59e0b', fontcolor='white')
dot.node('busca', 'Busca\n(Optional)', shape='box', style='filled', fillcolor='#f59e0b', fontcolor='white')
dot.node('avaliacao', 'Avaliação\n(Optional)', shape='box', style='filled', fillcolor='#f59e0b', fontcolor='white')
dot.node('notificacao', 'Notificação\n(Optional)', shape='box', style='filled', fillcolor='#f59e0b', fontcolor='white')

# Edges
dot.edge('root', 'catalogo', arrowhead='dot') # Mandatory
dot.edge('root', 'auth', arrowhead='odot')    # Optional
dot.edge('root', 'busca', arrowhead='odot')

# Empréstimo requires Auth
dot.edge('auth', 'emprestimo', arrowhead='odot')
dot.edge('emprestimo', 'multa', arrowhead='odot')

# Outros dependentes de Auth/Catalogo
dot.edge('auth', 'avaliacao', arrowhead='odot')
dot.edge('auth', 'notificacao', arrowhead='odot')

dot.render('Docs/img/diagrama_features', format='png', cleanup=True)
print('Diagrama FODA gerado: Docs/img/diagrama_features.png')
