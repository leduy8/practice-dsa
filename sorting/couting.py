class CountingSort:
    def sort(self, arr):
        if len(arr) == 0:
            return arr
            
        count_arr = [0 for _ in range(max(arr) + 1)]
        
        for num in arr:
            count_arr[num] += 1
        
        k = 0
        for i in range(len(count_arr)):
            for _ in range(count_arr[i]):
                arr[k] = i
                k += 1
        
        return arr



counting = CountingSort()
sorted1 = counting.sort([2, 1, 3, 6, 2, 0])
print(sorted1)
sorted2 = counting.sort([7, 3])
print(sorted2)
sorted3 = counting.sort([7])
print(sorted3)
sorted4 = counting.sort([])
print(sorted4)