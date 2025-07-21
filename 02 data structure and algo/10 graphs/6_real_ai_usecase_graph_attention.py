# Simulate token attention as graph traversal in NLP

attention_graph = {
    "Token1": ["Token2", "Token3"],   # Token1 attends to Token2 & Token3
    "Token2": ["Token4"],
    "Token3": ["Token4"],
    "Token4": []
}

def show_attention_flow(token, visited=None):
    if visited is None:
        visited = set()

    if token not in visited:
        print(f"{token} attends to → {attention_graph[token]}")
        visited.add(token)
        for next_token in attention_graph[token]:
            show_attention_flow(next_token, visited)

show_attention_flow("Token1")