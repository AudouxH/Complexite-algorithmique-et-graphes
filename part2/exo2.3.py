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

# Match the pair of nodes but setting a time to count the execution speed during the operation
def evaluate_heuristics(graph):
    t_start = time.perf_counter()
    max_degree_match = degree_matching(graph, True)
    max_degree_time = time.perf_counter() - t_start

    t_start = time.perf_counter()
    min_degree_match = degree_matching(graph, False)
    min_degree_time = time.perf_counter() - t_start

    return len(max_degree_match), max_degree_time, len(min_degree_match), min_degree_time

# Perform the matching for each nb of trials
for _ in range(num_trials):
    graph = nx.gnp_random_graph(n, p)
    max_degree_size, max_degree_time, min_degree_size, min_degree_time = evaluate_heuristics(graph)
    
    # set the returned values inside the global statistics list
    maximum_degree_sizes.append(max_degree_size)
    maximum_degree_times.append(max_degree_time)
    minimum_degree_sizes.append(min_degree_size)
    minimum_degree_times.append(min_degree_time)

# set the size of the window
plt.figure(figsize=(15, 10))

# Create a plot to compare the matching size over the number of trials
plt.subplot(2, 1, 1)
plt.plot(maximum_degree_sizes, label='maximum Degree Matching Size', alpha=0.7)
plt.plot(minimum_degree_sizes, label='minimum Degree Matching Size', alpha=0.7)
plt.xlabel('Trial')
plt.ylabel('Matching Size')
plt.title('Comparison of Matching Sizes')
plt.legend()

# Create a plot to compare the execution time over the number of trials
plt.subplot(2, 1, 2)
plt.plot(maximum_degree_times, label='maximum Degree Matching Time', alpha=0.7)
plt.plot(minimum_degree_times, label='minimum Degree Matching Time', alpha=0.7)
plt.xlabel('Trial')
plt.ylabel('Computation Time (s)')
plt.title('Comparison of Computation Times')
plt.legend()

# Display the graphs on the screen
plt.show()