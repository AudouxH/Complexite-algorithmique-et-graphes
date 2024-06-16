import matplotlib.pyplot as plt
import networkx as nx
import time
from matching_function import degree_matching

# graph parameters
n = 120
p = 0.04
num_trials = 100

# Lists to store results
maximum_degree_sizes = []
maximum_degree_times = []
minimum_degree_sizes = []
minimum_degree_times = []

def evaluate_heuristics(graph):
    start_time = time.perf_counter()
    greedy_match = degree_matching(graph, True)
    greedy_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    least_degree_match = degree_matching(graph, False)
    least_degree_time = time.perf_counter() - start_time

    return len(greedy_match), greedy_time, len(least_degree_match), least_degree_time

# Perform trials
for _ in range(num_trials):
    graph = nx.gnp_random_graph(n, p)
    size_greedy, greedy_time, size_least_degree, least_degree_time = evaluate_heuristics(graph)
    
    maximum_degree_sizes.append(size_greedy)
    minimum_degree_sizes.append(size_least_degree)
    maximum_degree_times.append(greedy_time)
    minimum_degree_times.append(least_degree_time)

# Plot the results
plt.figure(figsize=(15, 10))

plt.subplot(2, 1, 1)
plt.plot(maximum_degree_sizes, label='Greedy Degree Matching Size', alpha=0.7)
plt.plot(minimum_degree_sizes, label='Greedy Least Degree Matching Size', alpha=0.7)
plt.xlabel('Trial')
plt.ylabel('Matching Size')
plt.title('Comparison of Matching Sizes')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(maximum_degree_times, label='Greedy Degree Matching Time', alpha=0.7)
plt.plot(minimum_degree_times, label='Greedy Least Degree Matching Time', alpha=0.7)
plt.xlabel('Trial')
plt.ylabel('Computation Time (s)')
plt.title('Comparison of Computation Times')
plt.legend()

plt.tight_layout()
plt.show()