# Preorder traversal of a binary tree using recursion

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# Create tree
'''
    A
   / \
  B   C
 / \
D   E
'''
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

preorder(root)  # Output: A B C