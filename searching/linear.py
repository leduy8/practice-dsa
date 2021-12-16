class LinearSearch:
    def search(self, arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
    
        return -1


linear = LinearSearch()
print(linear.search([6, 2, 3, 8, 1, 5, 2, 1], 1))
print(linear.search([6, 2, 3, 8, 1, 5, 2, 1], -1))
