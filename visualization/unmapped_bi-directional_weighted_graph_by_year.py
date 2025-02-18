from matplotlib.font_manager import fontManager, FontProperties
from dataframe_to_edges import edges_from_df
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

year = '2020'

migration_df = pd.read_parquet(
    f'processed_data/directional_graph_{year}.parquet')
edges = edges_from_df(migration_df)

G = nx.DiGraph()

# Reverses order created in df - data set is originally in arrived to, departed from
# Without reversal, draws arcs in mistaken directions
for u, v, w in edges:
    G.add_edge(v, u, weight=w)

node_weights = {node: sum(d['weight'] for u, v, d in G.in_edges(
    node, data=True)) for node in G.nodes()}

node_sizes = [node_weights[node] * 0.01 for node in G.nodes()]

pos = nx.spring_layout(G)

fig, ax = plt.subplots()

nx.draw_networkx_nodes(G, pos, node_size=node_sizes)

drawn_edges = set()

for u, v in G.edges():
    if (v, u) in G.edges() and (u, v) not in drawn_edges:
        rad = 0.1

        edge_color = 'green' if G[u][v]['weight'] > G[v][u]['weight'] else 'red'

        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)],
                               edge_color=edge_color,
                               width=G[u][v]['weight'] * 0.001,
                               connectionstyle=f'arc3,rad={rad}',
                               arrows=True)
        nx.draw_networkx_edges(G, pos, edgelist=[(v, u)],
                               edge_color='green' if edge_color == 'red' else 'red',
                               width=G[v][u]['weight'] * 0.001,
                               connectionstyle=f'arc3,rad={rad}',
                               arrows=True)

        drawn_edges.add((u, v))
        drawn_edges.add((v, u))
    elif (u, v) not in drawn_edges:
        edge_color = 'green'
        nx.draw_networkx_edges(G, pos, edgelist=[(
            u, v)], edge_color=edge_color, width=G[u][v]['weight'] * 0.001)

        drawn_edges.add((u, v))

font_path = 'fonts/cmunrm.ttf'
fontManager.addfont(font_path)

prop = FontProperties(fname=font_path)

nx.draw_networkx_labels(G, pos, font_size=5,
                        font_family='serif', font_color='red')

# edge_labels = {}
# for u, v in G.edges():
#    edge_labels[(u, v)] = f'{G[u][v]["weight"]}'
#    if (v, u) in G.edges():
#        edge_labels[(v, u)] = f'{G[v][u]["weight"]}'

# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, fontproperties=prop)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.7, fontproperties=prop)

plt.title(f"Inter-regional migration {year}", fontproperties=prop)
plt.savefig(
    f'visualization/results/Weighted Graph Migration {year}.png', dpi=300)

plt.show()
