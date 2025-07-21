# Find min and max depth of binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def min_depth(node):
    if not node:
        return 0
    return 1 + min(min_depth(node.left), min_depth(node.right))

def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

# Build tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")

print("Min Depth:", min_depth(root))
print("Max Depth:", max_depth(root))