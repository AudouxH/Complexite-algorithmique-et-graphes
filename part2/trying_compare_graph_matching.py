import networkx as nx
import matplotlib.pyplot as plt

# Function to generate different types of random graphs
def generate_random_graph(graph_type, n, p):
    if graph_type == "Erdos-Renyi":
        return nx.gnp_random_graph(n, p)
    elif graph_type == "Barabasi-Albert":
        m = int(p * (n - 1))  # number of edges to attach from a new node to existing nodes
        return nx.barabasi_albert_graph(n, m)
    elif graph_type == "Watts-Strogatz":
        k = int(p * n)  # each node is joined with its k nearest neighbors in a ring topology
        return nx.watts_strogatz_graph(n, k, p)
    else:
        raise ValueError("Unknown graph type")

# Function to evaluate different matching methods
def evaluate_matching_methods(G):
    max_match = nx.maximal_matching(G)
    
    # Create a weighted graph for maximum cardinality matching
    weighted_G = nx.Graph()
    weighted_G.add_nodes_from(G.nodes())
    for u, v in G.edges():
        weighted_G.add_edge(u, v, weight=1.0)  # Assign a weight of 1.0 to each edge
    
    max_card_match = nx.max_weight_matching(weighted_G, maxcardinality=True)
    
    return len(max_match), len(max_card_match)

# Parameters
n = 120
p = 0.04
num_graphs = 100  # Number of graphs to generate for each type

# Graph types to compare
graph_types = ["Erdos-Renyi", "Barabasi-Albert", "Watts-Strogatz"]

# Dictionary to store results
results = {graph_type: {"Maximal Matching": [], "Max Cardinality Matching": []} for graph_type in graph_types}

# Generate graphs and evaluate matching methods
for graph_type in graph_types:
    for _ in range(num_graphs):
        G = generate_random_graph(graph_type, n, p)
        max_match_size, max_card_match_size = evaluate_matching_methods(G)
        
        results[graph_type]["Maximal Matching"].append(max_match_size)
        results[graph_type]["Max Cardinality Matching"].append(max_card_match_size)

# Visualize the results
plt.figure(figsize=(15, 10))
for graph_type in graph_types:
    max_match_sizes = results[graph_type]["Maximal Matching"]
    max_card_match_sizes = results[graph_type]["Max Cardinality Matching"]
    
    plt.plot(max_match_sizes, label=f'{graph_type} - Maximal Matching', alpha=0.7)
    plt.plot(max_card_match_sizes, label=f'{graph_type} - Max Cardinality Matching', alpha=0.7)

plt.xlabel('Graph Instance')
plt.ylabel('Matching Size')
plt.title('Comparison of Matching Methods Across Different Graph Types')
plt.legend()

plt.show()
