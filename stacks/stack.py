class Stack:
    def __init__(self) -> None:
        self.arr = []
        self.size = 0

    def push(self, item):
        self.arr.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        
        pop = self.arr.pop()
        self.size -= 1

        return pop
        

    def peek(self):
        if self.is_empty():
            return 'Stack is empty'

        return self.arr[-1]

    def is_empty(self):
        return self.size <= 0