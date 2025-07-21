# Representing a graph using an adjacency list (dictionary of lists)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Print graph connections
for node in graph:
    print(f"{node} → {graph[node]}")