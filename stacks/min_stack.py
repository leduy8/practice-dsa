from stack import Stack

class MinStack:
    def __init__(self) -> None:
        self.stack = Stack()
        self.min_vals = Stack()

    def push(self, item):
        if self.min_vals.is_empty():
            self.min_vals.push(item)
        elif item < self.min_vals.peek():
            self.min_vals.push(item)
        
        self.stack.push(item)

    def pop(self):
        if self.stack.peek() == self.min_vals.peek():
            self.min_vals.pop()
        
        self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def get_min(self):
        return self.min_vals.peek()


min_stack = MinStack()
min_stack.push(5)
min_stack.push(2)
min_stack.push(10)
min_stack.push(1)
print(min_stack.get_min())
min_stack.pop()
print(min_stack.get_min())
