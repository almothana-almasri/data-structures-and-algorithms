class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = Node(value)

    def insert_before(self, target_value, new_value):
        if self.head is None:
            return

        if self.head.value == target_value:
            self.head = Node(new_value, self.head)
            return

        curr_node = self.head
        while curr_node.next is not None and curr_node.next.value != target_value:
            curr_node = curr_node.next

        if curr_node.next is not None:
            new_node = Node(new_value, curr_node.next)
            curr_node.next = new_node

    def insert_after(self, target_value, new_value):
        if self.head is None:
            return

        curr_node = self.head
        while curr_node is not None and curr_node.value != target_value:
            curr_node = curr_node.next

        if curr_node is not None:
            new_node = Node(new_value, curr_node.next)
            curr_node.next = new_node

    # *** Stretch Goal ***
    def delete(self, target_value):
        if self.head is None:
            return

        if self.head.value == target_value:
            self.head = self.head.next
            return

        curr_node = self.head
        while curr_node.next is not None and curr_node.next.value != target_value:
            curr_node = curr_node.next

        if curr_node.next is not None:
            curr_node.next = curr_node.next.next
            
    # *** to make testing simpler ***
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

