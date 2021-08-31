import sys
sys.path.append('../')
from stacks.stack import Stack

class QueueUsingStack:
    def __init__(self) -> None:
        # ? Stack 1 is normal stack, for enqueue
        # ? Stack 2 is reverse stack, for dequeue
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())
        
        return self.stack_2.pop()

q = QueueUsingStack()
print(q.dequeue())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())