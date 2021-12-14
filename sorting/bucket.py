class BucketSort:
    def sort(self, arr, num_buckets):
        buckets = []

        for _ in range(num_buckets):
            buckets.append([])
        
        for item in arr:
            remain = int(item / num_buckets)
            if remain >= len(buckets):
                buckets[-1].append(item)
            else: 
                buckets[remain].append(item)

        i = 0
        for bucket in buckets:
            bucket.sort()
            for item in bucket:
                arr[i] = item
                i += 1
        
        return arr


bucket = BucketSort()
sorted1 = bucket.sort([2, 1, 3, 6, 2, 0], 3)
print(sorted1)
sorted2 = bucket.sort([7, 3], 1)
print(sorted2)
sorted3 = bucket.sort([7], 1)
print(sorted3)
sorted4 = bucket.sort([], 1)
print(sorted4)