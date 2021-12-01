class MergeSort:
    def sort(self, arr):
        if len(arr) > 1:
            middle = len(arr) // 2
            
            left = self.sort(arr[:middle])
            right = self.sort(arr[middle:])
            
            self.merge(left, right, arr)
            
    
    def merge(self, left, right, result):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            result[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            result[k] = right[j]
            j += 1
            k += 1



merge = MergeSort()
sorted1 = merge.sort([2, 1, 3, 6, 2, -1])
print(sorted1)
sorted2 = merge.sort([7, 3])
print(sorted2)
sorted3 = merge.sort([7])
print(sorted3)
sorted4 = merge.sort([])
print(sorted4)