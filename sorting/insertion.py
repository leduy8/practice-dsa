class InsertionSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            current = arr[i]
            j = i - 1
            while j >= 0 and current < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = current
        
        return arr


insertion = InsertionSort()
sorted1 = insertion.sort([2, 1, 3, 6, 2, -1])
print(sorted1)
sorted2 = insertion.sort([7, 3])
print(sorted2)
sorted3 = insertion.sort([7])
print(sorted3)
sorted4 = insertion.sort([])
print(sorted4)
