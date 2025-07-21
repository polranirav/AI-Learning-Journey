# Delete a node at a given index

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_at(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                return
            current = current.next

        if current.next:
            current.next = current.next.next

    def print_list(self):
        node = self.head
        while node:
            print(node.value, end=" → ")
            node = node.next
        print("None")

# Example
ll = LinkedList()
ll.head = Node("A")
ll.head.next = Node("B")
ll.head.next.next = Node("C")
ll.delete_at(1)
ll.print_list()