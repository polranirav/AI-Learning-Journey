# Check if a path from root to leaf adds up to a given sum

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def has_path_sum(node, target):
    if not node:
        return False

    if not node.left and not node.right:
        return node.val == target

    return (has_path_sum(node.left, target - node.val) or
            has_path_sum(node.right, target - node.val))

# Build tree
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.right.left = Node(13)

print("Has path sum 20?", has_path_sum(root, 20))  # True or False