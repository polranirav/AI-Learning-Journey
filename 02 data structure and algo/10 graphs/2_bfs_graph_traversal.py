from collections import deque  # Import deque for queue (used in BFS)

# Define the graph using an adjacency list format (dictionary of lists)
graph = {
    "A": ["B", "C"],      # A is connected to B and C
    "B": ["D", "E"],      # B is connected to D and E
    "C": ["F"],           # C is connected to F
    "D": [],              # D has no children
    "E": ["F"],           # E is connected to F
    "F": []               # F has no children
}

def bfs(start):
    visited = set()            # Set to track already visited nodes
    queue = deque([start])     # Initialize queue with starting node

    while queue:
        node = queue.popleft()  # Remove element from front (FIFO)
        if node not in visited:
            print(node, end=" ")    # Visit (process) the node
            visited.add(node)       # Mark node as visited
            queue.extend(graph[node])  # Add unvisited neighbors to queue

print("BFS Traversal (Level Order):")
bfs("A")