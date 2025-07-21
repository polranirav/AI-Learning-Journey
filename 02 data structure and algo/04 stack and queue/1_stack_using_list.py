# LIFO Stack using Python list

stack = []

# Push elements
stack.append("data")
stack.append("prep")
stack.append("model")

print("Stack:", stack)

# Pop elements
last = stack.pop()
print("Popped:", last)
print("Remaining Stack:", stack)