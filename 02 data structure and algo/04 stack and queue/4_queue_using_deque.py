from collections import deque

queue = deque()

queue.append("token1")
queue.append("token2")
queue.append("token3")

print("Queue:", queue)

first = queue.popleft()
print("Dequeued:", first)
print("Remaining:", queue)