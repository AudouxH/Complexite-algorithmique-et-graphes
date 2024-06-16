import networkx as nx
import matplotlib.pyplot as plt

def generate_graph():
        # Generate Erdős-Rényi graph
        graph = nx.gnp_random_graph(120, 0.04)

        # add to the generated graph with some title and description
        plt.figure(figsize=(8, 6))
        plt.title('Erdős-Rényi graph\n120: nodes\np=0.04')
        description = f"Number of nodes: {graph.number_of_nodes()}, Number of edges: {graph.number_of_edges()}"
        plt.text(0.5, -0.04, description, ha='center', transform=plt.gca().transAxes, color='black')
        
        nodes_position = nx.spring_layout(graph)  # positions for all nodes
        
        # Draw nodes with labels and edges between
        nx.draw_networkx_nodes(graph, nodes_position, node_size=700, node_color="lightblue")
        nx.draw_networkx_labels(graph, nodes_position, font_size=12, font_family="sans-serif")
        nx.draw_networkx_edges(graph, nodes_position, edgelist=graph.edges(), width=1.0, alpha=0.5, edge_color="gray")
        
        # Draw the graph on a window
        plt.show()

generate_graph()