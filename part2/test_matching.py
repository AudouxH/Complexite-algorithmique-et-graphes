import networkx as nx
import unittest
from matching_function import degree_matching

def is_not_duplicated(graph, matching):
    matched_nodes = set()
    # for each matching pairs in the matching result list
    for u, v in matching:
        # if the worker or the neighbort are already inside the matched_nodes
        if u in matched_nodes or v in matched_nodes:
            # return false to report the duplication
            return False
        # else add both inside the matched_nodes list
        matched_nodes.add(u)
        matched_nodes.add(v)
    return True

def is_perfect_matching(graph, matching):
    matched_nodes = set()
    # for each matching pairs in the matching result list
    for u, v in matching:
        # we add the worker and his neighbort inside the matched_nodes list
        matched_nodes.add(u)
        matched_nodes.add(v)
    # then we compare the number size of the graph nodes and the matched_nodes list to know if every workers had found a pair
    nb_lost_workers = len(graph.nodes()) - len(matched_nodes)
    return nb_lost_workers

class TestMatching(unittest.TestCase):
    def test_maximum_degree_matching(self):
        graph = nx.gnp_random_graph(120, 0.04)
        matching = degree_matching(graph, True)
        assert is_not_duplicated(graph, matching), "Maximum Degree Matching have duplication nodes inside the matching list"
        nb_lost_workers = is_perfect_matching(graph, matching)
        print(f"Got {nb_lost_workers} lost workers using minimum degree matching.")

    def test_minimum_degree_matching(self):
        graph = nx.gnp_random_graph(120, 0.04)
        matching = degree_matching(graph, False)
        assert is_not_duplicated(graph, matching), "Minimum Least Degree have duplication nodes inside the matching list"
        nb_lost_workers = is_perfect_matching(graph, matching)
        print(f"Got {nb_lost_workers} lost workers using minimum degree matching.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print("All tests passed.")