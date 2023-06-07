class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, value):
        self.stack.append(value)
        if not self.maxStack or value >= self.maxStack[-1]:
            self.maxStack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.maxStack[-1]:
            self.maxStack.pop()
        return value

    def getMax(self):
        if not self.maxStack:
            return None
        return self.maxStack[-1]
    
stack = MaxStack()
stack.push(5)
stack.push(2)
stack.push(7)
stack.push(3)

print(stack.getMax())  # Output: 7

stack.pop()
stack.pop()

print(stack.getMax())  # Output: 5
