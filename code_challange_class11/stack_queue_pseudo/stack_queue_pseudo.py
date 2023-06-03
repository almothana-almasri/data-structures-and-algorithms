class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []
    
    def push(self, value):
        """Add an element to the top of the stack."""
        self.stack.append(value)
    
    def pop(self):
        """Remove and return the element at the top of the stack."""
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        """Return the element at the top of the stack without removing it."""
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

class Pseudo_queue:
    def __init__(self):
        """Initialize an empty pseudo queue."""
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, value):
        """Add an element to the end of the pseudo queue."""
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        
        self.stack1.push(value)
        
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
    
    def dequeue(self):
        """Remove and return the element from the front of the pseudo queue."""
        if self.stack1.is_empty():
            return None
        
        return self.stack1.pop()