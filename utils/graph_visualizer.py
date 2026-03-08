from pyvis.network import Network


def visualize_graph(graph):

    net = Network(height="600px", width="100%", directed=True)

    for node in graph.nodes(data=True):

        label = node[0]
        node_type = node[1].get("type")

        if node_type == "file":
            color = "lightblue"
        else:
            color = "orange"

        net.add_node(label, label=label, color=color)

    for edge in graph.edges():
        net.add_edge(edge[0], edge[1])

    net.save_graph("graph.html")

    return "graph.html"