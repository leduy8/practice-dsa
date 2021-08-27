
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
            return -1
            
        for i in range(index, len(self.arr) - 1):
            self.arr[i] = self.arr[i + 1]
        
        self.arr[-1] = 0
        self.count -= 1

    def index_of(self, data):
        for i, d in enumerate(self.arr):
            if d == data:
                return i
        return -1

    def print_all(self):
        return self.arr

    def max(self):
        max_val = self.arr[0]

        for _, data in enumerate(self.arr, start=1):
            if max_val < data:
                max_val = data
        
        return max_val


    def reverse(self):
        # for i in range(self.count-1, -1, -1):
        #     print(self.arr[i], end=' ')
        
        temp = []

        for i in range(0, self.count)[::-1]:
            temp.append(self.arr[i])

        self.arr = temp

    def intersect(self):
        list_a = [1, 2, 3, 4, 1]
        list_b = [1, 4, 7, 3]

        common = {}

        for data in list_a:
            if data not in common:
                common[data] = 1

        for data in list_b:
            if data in common.keys():
                common[data] += 1
        
        for data in common.items():
            if data[1] > 1:
                print(data[0], end=' ')

    def insert_at(self, index, data):
        if index > self.count or index < 0:
            return -1

        if self.count == len(self.arr):
            self.arr.append(0)
            self.count += 1
        elif self.count < len(self.arr):
            self.count += 1

        for i in range(index, self.count)[::-1]:
            self.arr[i] = self.arr[i - 1]

        self.arr[index] = data


a = Array(count=2)
# print(a.count)
a.insert(1)
a.insert(3)
a.insert(2)
a.insert(3)
a.insert(4)
# print(a.index_of(1))
# print(a.index_of(3))
# print(a.remove_at(-1))
# print(a.remove_at(100))
# print(a.print_all())
a.remove_at(0)
# a.remove_at(1)
# print(a.print_all())
# print(a.count)
# print(a.max())
# a.reverse()
# print(a.print_all())
# a.intersect()
a.insert_at(index=1, data=6)
print(a.print_all())
# a.insert_at(index=5, data=6)
# print(a.print_all())