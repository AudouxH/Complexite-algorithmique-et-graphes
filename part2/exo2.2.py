import networkx as nx
import matplotlib.pyplot as plt

# Evaluate the matching degree for nodes inside the graph 
def degree_matching(graph, is_reverse):
    matching = set()
    # sorted the graph nodes by their degree (number of edges connected) from higher to lower when reverse is true and from lower to higher it is false 
    sorted_nodes = sorted(graph.degree, key=lambda x: x[1], reverse=is_reverse)
    matched_nodes = set()
    
    for node, degree in sorted_nodes:
        if node not in matched_nodes:
            try:
                for neighbor in graph.neighbors(node):
                    if neighbor not in matched_nodes:
                        matching.add((node, neighbor))
                        matched_nodes.add(node)
                        matched_nodes.add(neighbor)
                        break
            except KeyError as e:
                print(f"KeyError: {e}")
                print(f"Node {node} not found in graph.")
                continue

    return matching

# run the matching function counting the time for each
def evaluate_heuristics(graph):
    greedy_match = degree_matching(graph, True)
    least_degree_match = degree_matching(graph, False)

    return len(greedy_match), len(least_degree_match), greedy_match, least_degree_match

def generate_graph():
        graph = nx.gnp_random_graph(120, 0.04)

        # Evaluate the graph heuristics
        size_greedy, size_least_degree, greedy_match, least_degree_match = evaluate_heuristics(graph)
        
        # Display the generated graph
        plt.figure(figsize=(8, 6))
        # title
        plt.title('Erdős-Rényi graph\n120: nodes\np=0.04')
        
        # descritpion (number of nodes, edges, greedy match edges and least degree match edges)
        description = f"Number of nodes: {graph.number_of_nodes()}, Number of edges: {graph.number_of_edges()}"
        greedy_match_desc = f"Number of greedy match: {size_greedy}"
        least_degree_match_desc = f"Number of least degree match: {size_least_degree}"
        plt.text(0.5, -0.04, description, ha='center', transform=plt.gca().transAxes, color='black')
        plt.text(0.5, -0.07, greedy_match_desc, ha='center', transform=plt.gca().transAxes, color='red')
        plt.text(0.5, -0.1, least_degree_match_desc, ha='center', transform=plt.gca().transAxes, color='green')
        
        greedy_matching_edges = list(greedy_match)
        least_degree_matching_edges = list(least_degree_match)
        
        nodes_position = nx.spring_layout(graph)  # positions for all nodes
        
        # Draw nodes
        nx.draw_networkx_nodes(graph, nodes_position, node_size=700, node_color="lightblue")
        # Draw all edges
        nx.draw_networkx_edges(graph, nodes_position, edgelist=graph.edges(), width=1.0, alpha=0.5, edge_color="gray")
        # Highlight the edges in the greedy_matching_edges
        nx.draw_networkx_edges(graph, nodes_position, edgelist=greedy_matching_edges, width=2.0, alpha=0.8, edge_color="red")
        # Highlight the edges in the least_degree_matching_edges
        nx.draw_networkx_edges(graph, nodes_position, edgelist=least_degree_matching_edges, width=2.0, alpha=0.8, edge_color="green")
        # Draw node labels
        nx.draw_networkx_labels(graph, nodes_position, font_size=12, font_family="sans-serif")
        
        # display the graph on the window
        plt.show()

generate_graph()