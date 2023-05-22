class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def zipLists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        if next1:
            current2.next = next1

        current1 = next1
        current2 = next2

    return list1

