class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # Time complexity: O(n)
    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    # Time complexity: O(1)
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Time complexity: O(n)
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Time complexity: O(n)
    def insert_position(self, data, position):
        new_node = Node(data)
        current = self.head
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        for i in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Time complexity: O(n)
    def delete_node(self, position):
        if position < 0:
            return
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(position):
            prev = current
            current = current.next
        prev.next = current.next