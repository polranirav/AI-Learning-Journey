from collections import deque

# Graph as adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

def bfs(start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            q.extend(graph[node])

bfs("A")