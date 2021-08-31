import sys
sys.path.append('../')
from stacks.stack import Stack
from queue import Queue

def reverse_queue(queue):
    stack = Stack()
    while not queue.empty():
        stack.push(queue.get())
    
    while not stack.is_empty():
        queue.put(stack.pop())

# queue = Queue(maxsize=10)
# queue.put(10)
# queue.put(20)
# queue.put(30)
# print(f'Before reverse: {list(queue.queue)}')
# reverse_queue(queue)
# print(f'After reverse: {list(queue.queue)}')


def reverse_queue_by_k(queue, k):
    stack = Stack()
    queue_2 = Queue(10)
    
    count = 1
    while queue.qsize() > 0:
        if count <= k:
            stack.push(queue.get())
        else:
            queue_2.put(queue.get())
        count += 1
    
    while not stack.is_empty():
        queue.put(stack.pop())

    while queue_2.qsize() > 0:
        queue.put(queue_2.get())
    
    return queue


# q = Queue(5)
# q.put(10)
# q.put(20)
# q.put(30)
# q.put(40)
# q.put(50)
# print(f'Before: {list(q.queue)}')
# reverse_queue_by_k(q, 3)
# print(f'After: {list(q.queue)}')

# ? Assume inputs as each push in the stack
def stack_with_two_queue(inputs):
    q_1 = Queue(10)
    q_2 = Queue(10)
    stack = Stack()

    for input in inputs:
        q_1.put(input)
    
    while q_1.qsize() > 0:
        q_2.put(q_1.get())

    while q_2.qsize() > 0:
        stack.push(q_2.get())

    # * Demonstrate
    while not stack.is_empty():
        print(stack.pop(), end=' ')

stack_with_two_queue([1, 2, 3, 4])

