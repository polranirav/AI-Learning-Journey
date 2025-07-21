# Binary Search Tree (BST) — insert and search

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def search(root, key):
    if not root:
        return False
    if root.val == key:
        return True
    elif key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Build BST
root = None
for num in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, num)

print("Search 40:", search(root, 40))  # True
print("Search 25:", search(root, 25))  # False