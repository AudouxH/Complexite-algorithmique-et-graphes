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