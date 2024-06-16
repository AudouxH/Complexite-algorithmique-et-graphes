import networkx as nx
import time
import statistics
import matplotlib.pyplot as plt
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

# get more statistical analysis about the values that we got using our heuristic function
mean_matching_size_max_degree = statistics.mean(maximum_degree_sizes)
mean_matching_size_min_degree = statistics.mean(minimum_degree_sizes)
mean_execution_time_max_degree = statistics.mean(maximum_degree_times)
mean_execution_time_min_degree = statistics.mean(minimum_degree_times)

# Print the results on the prompt
print("Statistical Comparison:")
print(f"Mean Matching Size (Max Degree): {mean_matching_size_max_degree}")
print(f"Mean Matching Size (Min Degree): {mean_matching_size_min_degree}")
print(f"Mean Execution Time (Max Degree): {mean_execution_time_max_degree:.6f} seconds")
print(f"Mean Execution Time (Min Degree): {mean_execution_time_min_degree:.6f} seconds")

# Set the window size
plt.figure(figsize=(12, 5))

# Create a plot to compare the matching size over the number of trials
plt.subplot(1, 2, 1)
plt.hist(maximum_degree_sizes, bins=15, alpha=0.5, label="Max Degree Heuristic")
plt.hist(minimum_degree_sizes, bins=15, alpha=0.5, label="Min Degree Heuristic")
plt.title("Matching Sizes Distribution")
plt.xlabel("Matching Size")
plt.ylabel("Frequency")
plt.legend()

# Create histograms to visualize execution times
plt.subplot(1, 2, 2)
plt.hist(maximum_degree_times, bins=15, alpha=0.5, label="Max Degree Heuristic")
plt.hist(minimum_degree_times, bins=15, alpha=0.5, label="Min Degree Heuristic")
plt.title("Execution Times Distribution")
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Frequency")
plt.legend()

# display the graphs on the screen
plt.show()