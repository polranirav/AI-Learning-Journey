# Detect cycle in a directed graph using DFS and recursion stack

graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]  # ← cycle A → B → C → A
}

def has_cycle(node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if has_cycle(neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True  # Found back edge

    rec_stack.remove(node)
    return False

visited = set()
rec_stack = set()

cycle_found = any(
    has_cycle(node, visited, rec_stack) for node in graph
)

print("Cycle Detected?" , cycle_found)