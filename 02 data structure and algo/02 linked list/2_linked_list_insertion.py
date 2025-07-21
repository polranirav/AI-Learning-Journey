# Insert a node at a specific index

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(index - 1):
            if current is None: return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        node = self.head
        while node:
            print(node.value, end=" → ")
            node = node.next
        print("None")

# Example
ll = LinkedList()
ll.insert_at(0, "first")
ll.insert_at(1, "second")
ll.insert_at(1, "inserted")
ll.print_list()
# Output: first → inserted → second → None