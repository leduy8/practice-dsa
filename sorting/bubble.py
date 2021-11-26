class BubbleSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            is_sorted = True
            for j in range(1, n - i):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    is_sorted = False
            if is_sorted:
                return arr

        return arr


bubble = BubbleSort()
sorted1 = bubble.sort([2, 1, 3, 6, 2, -1])
print(sorted1)
sorted2 = bubble.sort([7, 3])
print(sorted2)
sorted3 = bubble.sort([7])
print(sorted3)
sorted4 = bubble.sort([])
print(sorted4)
