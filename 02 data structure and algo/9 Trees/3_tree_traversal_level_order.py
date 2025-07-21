# Level-order traversal (BFS using queue)

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

def level_order(root):
    if not root:
        return

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(node.val, end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

print("Level-order traversal:")
level_order(root)