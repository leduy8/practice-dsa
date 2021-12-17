from binary import BinarySearch


class ExponentialSearch:
    def search(self, arr, target):
        binary = BinarySearch()
        bound = 1

        while bound < len(arr) and arr[bound] < target:
            bound *= 2

        left = bound // 2
        right = min(bound, len(arr) - 1)
        return binary._search_recursive(arr, target, left, right)


exponential = ExponentialSearch()
print(exponential.search([1, 3, 5, 7, 11, 12, 13, 16], 5))
print(exponential.search([1, 3, 5, 7, 11, 12, 13, 16], 1))
print(exponential.search([1, 3, 5, 7, 11, 12, 13, 16], 16))
print(exponential.search([1, 3, 5, 7, 11, 12, 13, 16], -1))
print(exponential.search([1, 3], 3))
print(exponential.search([1], 1))
print(exponential.search([], 1))
