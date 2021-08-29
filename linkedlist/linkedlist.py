class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.size

    def add_first(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.size += 1

    def add_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = node
            self.last = node
        else:
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = node
            self.last = node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            return 'Linked list is empty'
        elif self.first.next is None:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
        self.size -= 1

    def delete_last(self):
        if self.is_empty():
            return 'Linked list is empty'
        elif self.first.next is None:
            self.first = None
            self.last = None
        else:
            current = self.first
            while current.next.next is not None:
                current = current.next
            self.last = current
            current.next = None
        self.size -= 1

    def contains(self, data):
        if self.is_empty():
            return 'Linked list is empty'

        current = self.first
        if current.value == data:
            return True

        while current.next is not None:
            current = current.next
            if current.value == data:
                return True

        return False

    def index_of(self, data):
        if self.is_empty():
            return 'Linked list is empty'

        current = self.first
        pos = 0
        if current.value == data:
            return pos

        while current.next is not None:
            current = current.next
            pos += 1
            if current.value == data:
                return pos

        return -1

    def print(self):
        if self.is_empty():
            return 'Linked list is empty'

        current = self.first
        while current.next is not None:
            print(current.value, end=' -> ')
            current = current.next

        print(current.value)

    def reverse(self):
        # [10 <- 20 <- 30 <- 40]
        #                    p    c    n
        if self.is_empty():
            return 'Linked list is empty'

        prev = self.first
        current = self.first.next
        self.last = self.first
        self.last.next = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.first = prev

    def kth_node_from_the_end(self, k):
        # Hint:
        # [10, 20, 30, 40, 50]
        #          f       l
        # k = 1 (50)
        # k = 2 (40)
        # k = 3 (30)
        if k > self.size or k < 1:
            return 'Invalid Kth'

        f = self.first
        l = self.first
        count = 0
        while l.next is not None:
            l = l.next
            count += 1
            if count >= k:
                f = f.next

        return f.value

    def print_middle(self):
        # Assume we don't know whether the size is odd or even
        slow = self.first
        fast = self.first
        res = []

        while fast is not self.last and fast.next is not self.last:
            slow = slow.next
            fast = fast.next.next

        if fast.next is not None:
            res.append(slow.value)
            res.append(slow.next.value)
            return res
        else:
            return slow.value


linkedlist = LinkedList()
linkedlist.add_last(10)
linkedlist.add_last(20)
linkedlist.add_last(30)
linkedlist.add_first(5)
# linkedlist.delete_first()
# linkedlist.delete_first()
# linkedlist.delete_last()
# print(linkedlist.contains(4))
# print(linkedlist.contains(30))
# print(linkedlist.index_of(1))
# print(linkedlist.index_of(30))
linkedlist.print()
# linkedlist.reverse()
# linkedlist.print()
# print(linkedlist.kth_node_from_the_end(-1))
# print(linkedlist.kth_node_from_the_end(1))
# print(linkedlist.kth_node_from_the_end(2))
# print(linkedlist.kth_node_from_the_end(3))
# print(linkedlist.kth_node_from_the_end(4))
# print(linkedlist.kth_node_from_the_end(5))
# print(linkedlist.print_middle())
