import networkx as nx
import matplotlib.pyplot as plt

from neural.cerebrum import Input


def draw_network(neurons, connections):

    nodes = [neuron.get_id() for neuron in neurons]
    node_colors = _pick_node_color(neurons)
    edges = _build_edges(connections)
    graph = _construct_graph(nodes, edges)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, arrows=True, node_size=1600,
            node_alpha=0.3, draw_spring=True, node_color=node_colors)
    plt.show()


def _build_edges(connections):
    edges = []

    for (neuron, incoming) in connections.items():
        for inc in incoming:
            edges.append((neuron, inc))

    return edges


def _construct_graph(nodes, edges):
    graph = nx.DiGraph()

    for node in nodes:
        graph.add_node(node)

    for (start, end) in edges:
        graph.add_edge(start, end)

    return graph


def _pick_node_color(neurons):
    input_color = "#51795a"
    hidden_color = "#c6e2ff"
    output_color = "#933835"
    node_colors = []

    for neuron in neurons:
        if isinstance(neuron, Input):
            node_colors.append(input_color)
        elif neuron.is_output():
            node_colors.append(output_color)
        else:
            node_colors.append(hidden_color)

    return node_colors
