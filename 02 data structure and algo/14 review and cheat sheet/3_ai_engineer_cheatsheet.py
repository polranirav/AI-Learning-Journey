"""
📌 AI Engineer DSA Cheat Sheet
Run this file to review real Python code examples that show how core
DSA concepts are used in AI/ML pipelines.
"""

# ✅ 1. List — store predictions or batch tokens
predictions = [0.85, 0.92, 0.78]
top_pred = max(predictions)
print("Top prediction score:", top_pred)

# ✅ 2. Dictionary — token/label to ID mapping
token_to_id = {"hello": 3, "world": 4}
tokens = ["hello", "world"]
ids = [token_to_id[tok] for tok in tokens]
print("Token IDs:", ids)

# ✅ 3. Set — remove duplicates from token list
raw_tokens = ["yes", "no", "yes", "maybe"]
unique_tokens = set(raw_tokens)
print("Unique tokens:", unique_tokens)

# ✅ 4. Queue (FIFO) — simulate batch processing
from collections import deque
queue = deque(["task1", "task2"])
queue.append("task3")
print("Next task:", queue.popleft())

# ✅ 5. Stack (LIFO) — simulate backtracking
stack = []
stack.append("state1")
stack.append("state2")
print("Backtrack to:", stack.pop())

# ✅ 6. Graph (adjacency list) — attention simulation
attention = {
    "token1": ["token2", "token3"],
    "token2": ["token4"],
    "token3": [],
    "token4": []
}
def traverse_graph(node):
    for neighbor in attention.get(node, []):
        print(f"{node} → {neighbor}")

traverse_graph("token1")

# ✅ 7. BFS — used in token traversal or path finding
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print("Visit:", node)
            visited.add(node)
            queue.extend(graph[node])

bfs(attention, "token1")

# ✅ 8. Sorting model results
models = [{"name": "A", "acc": 0.85}, {"name": "B", "acc": 0.92}]
sorted_models = sorted(models, key=lambda x: x["acc"], reverse=True)
print("Sorted models by accuracy:", sorted_models)

# ✅ 9. DP: Climb stairs (NLP token decode analogy)
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

print("Ways to decode 5 tokens:", climb_stairs(5))