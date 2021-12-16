
# ? Only work in sorted list

class TernarySearch:
    def search(self, arr, target):
        if len(arr) <= 0:
            return -1
        return self._search(arr, target, 0, len(arr) - 1)

    def _search(self, arr, target, left, right):
        partition = (right - left) // 3
        mid1 = left + partition
        mid2 = right - partition

        if arr[mid1] == target:
            return mid1
        
        if arr[mid2] == target:
            return mid2

        if left > right:
            return -1

        if target < arr[mid1]:
            return self._search(arr, target, left, mid1 - 1)
        elif target > arr[mid1] and target < arr[mid2]:
            return self._search(arr, target, mid1 + 1, mid2 - 1)
        return self._search(arr, target, mid2 + 1, right)


ternary = TernarySearch()
print(ternary.search([1, 3, 5, 7, 11, 12, 13, 16], 5))
print(ternary.search([1, 3, 5, 7, 11, 12, 13, 16], 1))
print(ternary.search([1, 3, 5, 7, 11, 12, 13, 16], 16))
print(ternary.search([1, 3, 5, 7, 11, 12, 13, 16], -1))
print(ternary.search([1, 3], 3))
print(ternary.search([1], 1))
print(ternary.search([], 1))
