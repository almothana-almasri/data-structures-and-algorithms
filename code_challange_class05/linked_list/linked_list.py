class Node:
    """
    Node represents a single node in a linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node in the list.
    """
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    LinkedList represents a linked list data structure.

    Attributes:
        head: The head (first node) of the linked list.
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Inserts a new node with the given value at the beginning of the linked list.

        Args:
            value: The value to be inserted.
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self, value):
        """
        Checks if the linked list contains a node with the given value.

        Args:
            value: The value to search for.

        Returns:
            True if a node with the given value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
        Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list in the format:
            "{ value1 } -> { value2 } -> ... -> NULL"
        """
        result = ""
        current = self.head
        while current:
            result += "{ " + str(current.value) + " } -> "
            current = current.next
        return result + "NULL"
