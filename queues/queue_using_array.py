
# * Queue using Array

class ArrayDeque:
    def __init__(self, maxsize) -> None:
        self.queue = []
        for _ in range(maxsize):
            self.queue.append(0)
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        if self.is_full():
            return 'Queue is full'

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % len(self.queue)
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        
        front = self.queue[self.front]
        self.queue[self.front] = 0
        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1

        return front

    def peek(self):
        return self.queue[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.queue)

    def print(self):
        print(self.queue)
        print(f'Front at index {self.front}')
        print(f'Rear at index {self.rear}')

array_deque = ArrayDeque(maxsize=5)
array_deque.enqueue(10)
array_deque.enqueue(20)
array_deque.enqueue(30)
array_deque.enqueue(40)
array_deque.enqueue(50)
array_deque.dequeue()
array_deque.dequeue()
array_deque.enqueue(60)
array_deque.enqueue(70)
array_deque.dequeue()
array_deque.dequeue()
array_deque.dequeue()
# print(array_deque.peek())
array_deque.print()
