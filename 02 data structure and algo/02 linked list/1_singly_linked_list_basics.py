# Basic implementation of a Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # points to next node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" → ")
            current = current.next
        print("None")

# Example
ll = LinkedList()
ll.append("data")
ll.append("prep")
ll.append("done")
ll.print_list()
# Output: data → prep → done → None