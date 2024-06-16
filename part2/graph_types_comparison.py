import networkx as nx
import matplotlib.pyplot as plt
import time
from matching_function import degree_matching

# run the minimum and maximum degree matching function on each graph
def evaluate_heuristics(graph):
    start_time = time.perf_counter()
    greedy_match = degree_matching(graph, True)
    greedy_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    least_degree_match = degree_matching(graph, False)
    least_degree_time = time.perf_counter() - start_time

    return len(greedy_match), greedy_time, len(least_degree_match), least_degree_time

def generate_and_evaluate_graph(graph_type, is_display, **kwargs):
    try:
        # Generate a new graph based on the specified graph type
        if graph_type == "erdos_renyi":
            graph = nx.gnp_random_graph(kwargs["n"], kwargs["p"])
        elif graph_type == "barabasi_albert":
            graph = nx.barabasi_albert_graph(kwargs["n"], kwargs["m"])
        elif graph_type == "watts_strogatz":
            graph = nx.watts_strogatz_graph(kwargs["n"], kwargs["k"], kwargs["p"])
        elif graph_type == "d_regular":
            graph = nx.random_regular_graph(kwargs["d"], kwargs["n"])
        elif graph_type == "geometric":
            graph = nx.random_geometric_graph(kwargs["n"], kwargs["radius"])
        elif graph_type == "scale_free":
            graph = nx.powerlaw_cluster_graph(kwargs["n"], kwargs["m"], kwargs["p"])
        elif graph_type == "sbm_params":
            graph = nx.stochastic_block_model(kwargs["sizes"], kwargs["probs"])
        else:
            raise ValueError("Unknown graph type")

        # Display each generated graph if we set the is_display value to True
        if is_display:
            plt.figure(figsize=(8, 6))
            plt.title(f'{graph_type.capitalize()} Graph')
            nx.draw(graph, node_size=50, node_color='blue', edge_color='gray', with_labels=False)
            plt.show()

        # Evaluate the heuristics values for this graph
        size_greedy, time_greedy, size_least_degree, time_least_degree = evaluate_heuristics(graph)

        # Output graph statistics comparison result
        print(f"{graph_type.capitalize()} Graph:")
        print(f"Number of nodes: {graph.number_of_nodes()}, Number of edges: {graph.number_of_edges()}")
        print(f"Greedy Degree Matching - Size: {size_greedy}, Time: {time_greedy:.6f}s")
        print(f"Greedy Least Degree Matching - Size: {size_least_degree}, Time: {time_least_degree:.6f}s")
        print("--------------------------------------------------------------------")

    except Exception as e:
        print(f"Error generating or evaluating graph '{graph_type}': {e}")

# Parameters for different graph types
n = 120
erdos_renyi_params = {"n": n, "p": 0.04}
barabasi_albert_params = {"n": n, "m": 2}
watts_strogatz_params = {"n": n, "k": 4, "p": 0.1}
d_regular_params = {"n": n, "d": 5}
geometric_params = {"n": n, "radius": 0.2}
scale_free_params = {"n": n, "m": 2, "p": 0.1}
sbm_params = {"sizes": [20, 20], "probs": [[0.3, 0.1], [0.1, 0.3]]}

# Modify this variable to display or not each graph representation
is_graphs_display = True

# Generate and evaluate graph types
generate_and_evaluate_graph("erdos_renyi", is_graphs_display, **erdos_renyi_params)
generate_and_evaluate_graph("barabasi_albert", is_graphs_display, **barabasi_albert_params)
generate_and_evaluate_graph("watts_strogatz", is_graphs_display, **watts_strogatz_params)
generate_and_evaluate_graph("d_regular", is_graphs_display, **d_regular_params)
generate_and_evaluate_graph("geometric", is_graphs_display, **geometric_params)
generate_and_evaluate_graph("scale_free", is_graphs_display, **scale_free_params)
generate_and_evaluate_graph("sbm_params", is_graphs_display, **sbm_params)