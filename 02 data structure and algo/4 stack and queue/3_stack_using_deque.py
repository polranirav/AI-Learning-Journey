from collections import deque

stack = deque()

stack.append("AI")
stack.append("ML")
stack.append("DL")

print("Stack:", stack)

top = stack.pop()
print("Popped:", top)
print("Now:", stack)
