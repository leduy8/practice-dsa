
# ? Simulate Java's array
class Array:
    count = 0
    arr = []

    def __init__(self, count, array = []) -> None:
        self.count = count
        if len(array) > 0:
            self.arr = array
            self.count = len(array)

    def insert(self, data):
        self.arr.append(data)
        
        if len(self.arr) - self.count == 1:
            self.count += 1

    def remove_at(self, index):
        if index > self.count or index < 0:
            return 'Invalid index'
            
        for i in range(index, len(self.arr) - 1):
            self.arr[i] = self.arr[i + 1]
        
        self.arr[-1] = 0
        self.count -= 0

    def index_of(self, data):
        for i, d in enumerate(self.arr):
            if d == data:
                return i
        return -1

    def print_all(self):
        return self.arr


a = Array(count=2)
print(a.count)
a.insert(1)
a.insert(3)
a.insert(2)
a.insert(3)
print(a.index_of(1))
print(a.index_of(3))
print(a.remove_at(-1))
print(a.remove_at(100))
print(a.print_all())
a.remove_at(0)
a.remove_at(1)
print(a.print_all())
print(a.count)