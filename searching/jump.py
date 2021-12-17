from math import sqrt


class JumpSearch:
    def search(self, arr, target):
        block_size = int(sqrt(len(arr)))
        start = 0
        next = block_size
        
        while start < len(arr) and arr[next - 1] < target:
            start = next
            next +=  block_size
            if next > len(arr):
                next = len(arr)
        
        pos = start
        for item in arr[start:next]:
            if item == target:
                return pos
            pos += 1

        return -1


jump = JumpSearch()
print(jump.search([1, 3, 5, 7, 11, 12, 13, 16], 5))
print(jump.search([1, 3, 5, 7, 11, 12, 13, 16], 1))
print(jump.search([1, 3, 5, 7, 11, 12, 13, 16], 16))
print(jump.search([1, 3, 5, 7, 11, 12, 13, 16], -1))
print(jump.search([1, 3], 3))
print(jump.search([1], 1))
print(jump.search([], 1))
