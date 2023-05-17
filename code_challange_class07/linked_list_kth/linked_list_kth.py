class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def kthFromEnd(self, k):
        if k < 0:
            raise Exception("k must be a positive integer")

        # First pass to get the length of the list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        if k >= length:
            raise Exception("k is greater than or equal to the length of the linked list")

        # Second pass to get the kth element from the end
        current = self.head
        for _ in range(length - k - 1):
            current = current.next

        return current.value
