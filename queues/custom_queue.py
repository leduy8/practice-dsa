class Queue:
    def __init__(self, size) -> None:
        self.arr = []
        self.size = size
        self.count = 0

    def enqueue(self, item):
        if self.is_full():
            return 'Queue is full'

        self.arr.append(item)
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        
        self.arr.pop(0)
        self.count -= 1

    def peek(self):
        return self.arr[-1]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= self.size