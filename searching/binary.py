
# ? Only work in sorted list

class BinarySearch:
    def search(self, arr, target):
        # return self._search_recursive(arr, target, 0, len(arr) - 1)
        return self._search_iterative(arr, target)

    def _search_recursive(self, arr, target, left, right):
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        if left > right:
            return -1

        if target < arr[mid]:
            return self._search_recursive(arr, target, left, mid - 1)
        
        return self._search_recursive(arr, target, mid + 1, right)

    def _search_iterative(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1


binary = BinarySearch()
print(binary.search([1, 3, 5, 7, 11, 12, 13, 16], 5))
print(binary.search([1, 3, 5, 7, 11, 12, 13, 16], 1))
print(binary.search([1, 3, 5, 7, 11, 12, 13, 16], 16))
print(binary.search([1, 3, 5, 7, 11, 12, 13, 16], -1))
