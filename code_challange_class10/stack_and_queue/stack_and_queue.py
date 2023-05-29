class Node:
    """
    Represents a node in a linked list.
    
    Args:
        value: The value stored in the node.
        next_: Reference to the next node in the linked list (default is None).
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Stack:
    """
    Represents a stack data structure.
    
    Methods:
        push(value): Adds a new element to the top of the stack.
        pop(): Removes and returns the element at the top of the stack.
        peek(): Returns the element at the top of the stack without removing it.
        is_empty(): Checks if the stack is empty.
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None


class Queue:
    """
    Represents a queue data structure.
    
    Methods:
        enqueue(value): Adds a new element to the rear of the queue.
        dequeue(): Removes and returns the element at the front of the queue.
        peek(): Returns the element at the front of the queue without removing it.
        is_empty(): Checks if the queue is empty.
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None
