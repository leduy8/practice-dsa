class SelectionSort():
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]

        return arr


selection = SelectionSort()
sorted1 = selection.sort([2, 1, 3, 6, 2, -1])
print(sorted1)
sorted2 = selection.sort([7, 3])
print(sorted2)
sorted3 = selection.sort([7])
print(sorted3)
sorted4 = selection.sort([])
print(sorted4)
