from stack_and_queue import Stack

class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.maxStack = Stack()

    def push(self, value):
        self.stack.push(value)
        if self.maxStack.is_empty() or value >= self.maxStack.peek():
            self.maxStack.push(value)

    def pop(self):
        if self.stack.is_empty():
            return None
        value = self.stack.pop()
        if value == self.maxStack.peek():
            self.maxStack.pop()
        return value

    def getMax(self):
        if self.maxStack.is_empty():
            return None
        return self.maxStack.peek()
    
stack = MaxStack()
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(3)

print(stack.getMax())  # Output: 7

stack.pop()
stack.pop()

print(stack.getMax())  # Output: 5
