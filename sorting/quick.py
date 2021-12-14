class QuickSort:
    def sort(self, arr):
        self._sort(arr, 0, len(arr) - 1)

    def _sort(self, arr, start, end):
        if start >= end:
            return

        # Partition
        boundary = self._partition(arr, start, end)
        # Sort left
        self._sort(arr, start, boundary - 1)
        # Sort right
        self._sort(arr, boundary + 1, end)


    def _partition(self, arr, start, end) -> int:
        pivot = arr[end]
        boundary = start - 1
        for i in range(start, end + 1):
            
            if arr[i] <= pivot:
                print(f'i {i}')
                print(f'boundary {boundary}')
                boundary += 1
                arr[i], arr[boundary] = arr[boundary], arr[i]

        return boundary

quick = QuickSort()
arr = [3, -2, 2, 5, 7, 1]
quick.sort(arr)
print(arr)
arr1 = [2, 1, 3, 6, 2, -1]
quick.sort(arr1)
print(arr1)
arr2 = [7, 3]
quick.sort(arr2)
print(arr2)
arr3 = [7]
quick.sort(arr3)
print(arr3)
arr4 = []
quick.sort(arr4)
print(arr4)