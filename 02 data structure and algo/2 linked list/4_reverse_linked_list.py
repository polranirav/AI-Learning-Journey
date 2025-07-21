# Reverse the entire linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Create list: A → B → C → None
head = Node("A")
head.next = Node("B")
head.next.next = Node("C")

# Reverse and print
new_head = reverse_linked_list(head)
node = new_head
while node:
    print(node.value, end=" → ")
    node = node.next
print("None")