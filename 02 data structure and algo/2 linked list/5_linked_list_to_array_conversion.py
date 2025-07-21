# Convert linked list to Python list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def to_array(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Example
head = Node("Nirav")
head.next = Node("AI")
head.next.next = Node("ML")

print(to_array(head))  # ['Nirav', 'AI', 'ML']