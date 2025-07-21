# Define a basic binary tree node structure

class Node:
    def __init__(self, value):
        self.value = value         # Store data in the node
        self.left = None           # Pointer to left child
        self.right = None          # Pointer to right child

# Create a simple binary tree:
'''
    A
   / \
  B   C
'''
root = Node("A")
root.left = Node("B")
root.right = Node("C")

# Print root and its children
print("Root:", root.value)
print("Left child:", root.left.value)
print("Right child:", root.right.value)