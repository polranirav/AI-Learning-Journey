# Tree traversal using recursion: Preorder, Inorder, Postorder

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

def preorder(node):
    if node:
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=" ")

print("Preorder: ", end="")
preorder(root)

print("\nInorder: ", end="")
inorder(root)

print("\nPostorder: ", end="")
postorder(root)