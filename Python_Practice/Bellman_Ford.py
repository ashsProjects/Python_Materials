import sys

def bellman_ford_sdsp(graph, target):
    # Reverse the direction of edges in the graph
    reversed_graph = {node: {} for node in graph}
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            reversed_graph[neighbor][node] = weight

    # Step 1: Initialize distances and predecessors
    distances = {node: sys.maxsize for node in graph}
    predecessors = {node: None for node in graph}
    distances[target] = 0

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node, edges in reversed_graph.items():
            for neighbor, weight in edges.items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node

    # Step 3: Check for negative weight cycles
    for node, edges in reversed_graph.items():
        for neighbor, weight in edges.items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances, predecessors

# Example usage:
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'a': {'b': 3},
        'b': {'c': 2},
        'c': {'a': 7},
        'd': {'a': 7, 'f': 5},
        'e': {'c': 3, 'd':3, 'f':10},
        'f': {'c': 8}
    }

    target_node = 'f'
    distances, predecessors = bellman_ford_sdsp(graph, target_node)

    # Print the distances and predecessors
    for node in graph:
        print(f"Shortest distance from {node} to {target_node}: {distances[node]}")
        path = [node]
        while predecessors[node]:
            path.insert(0, predecessors[node])
            node = predecessors[node]
        print(f"Shortest path: {' <- '.join(path)}")


