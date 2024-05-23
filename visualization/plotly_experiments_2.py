import networkx as nx
import plotly.graph_objects as go

# Create three sample graphs
graph1 = nx.path_graph(5)
graph2 = nx.path_graph(55)
graph3 = nx.path_graph(20)

# Generate positions for the nodes for each graph
pos1 = nx.spring_layout(graph1)
pos2 = nx.spring_layout(graph2)
pos3 = nx.spring_layout(graph3)

# Convert graphs to Plotly figures
figs = []
for i, (graph, pos) in enumerate([(graph1, pos1), (graph2, pos2), (graph3, pos3)]):
    edge_x = []
    edge_y = []
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)  # Add None to create gap between edges
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)  # Add None to create gap between edges

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', name=f'Graph {i+1}'))

    fig.update_layout(
        title=f'Graph {i+1}',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=False
    )

    figs.append(fig)

# Create slider
steps = []
for i, fig in enumerate(figs):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(figs)},
              {"title": f'Graph {i+1}'}],
        label=f'Graph {i+1}'
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)

# Add all steps to show all graphs
for i in range(len(figs)):
    sliders = [dict(
        active=i,
        currentvalue={"prefix": "Graph: "},
        steps=steps
    )]

    figs[i].update_layout(sliders=sliders)

# Show plot
figs[0].show()
