# FIFO Queue using Python list (⚠️ slow for large data)

queue = []

# Enqueue
queue.append("input1")
queue.append("input2")
queue.append("input3")

print("Queue:", queue)

# Dequeue
first = queue.pop(0)
print("Dequeued:", first)
print("Remaining Queue:", queue)