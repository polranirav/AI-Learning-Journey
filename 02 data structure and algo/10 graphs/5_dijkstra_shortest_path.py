# Dijkstra's algorithm: Find shortest path in weighted graph

import heapq  # For efficient priority queue

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": []
}

def dijkstra(start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    pq = [(0, start)]  # Min-heap: (distance, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

print("Shortest distances:", dijkstra("A"))