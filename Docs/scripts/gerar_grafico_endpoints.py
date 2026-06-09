import matplotlib.pyplot as plt
import os

servicos = [
    'Catálogo', 'Auth', 'Empréstimo',
    'Multa', 'Notificação', 'Busca', 'Avaliação', 'Gateway'
]
endpoints = [4, 6, 5, 3, 3, 2, 2, 2]

fig, ax = plt.subplots(figsize=(10, 5))
colors = ['#22c55e', '#6366f1', '#8b5cf6', '#f59e0b', '#ef4444', '#06b6d4', '#ec4899', '#64748b']
bars = ax.barh(servicos, endpoints, color=colors)
ax.set_xlabel('Número de Endpoints Rest API')
ax.set_title('Distribuição de Endpoints por Microsserviço')
ax.bar_label(bars, padding=3)
plt.tight_layout()

os.makedirs('Docs/img', exist_ok=True)
plt.savefig('Docs/img/endpoints_por_servico.png', dpi=150)
print('Gráfico gerado: Docs/img/endpoints_por_servico.png')
