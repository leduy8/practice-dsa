def find_first_non_repeat_char(string):
    string = string.lower()
    occ = {}
    for char in string:
        if char not in occ:
            occ[char] = 1
        else:
            occ[char] += 1

    for char in string:
        if occ[char] == 1:
            return char

    return None

# print(find_first_non_repeat_char('A Green Apple')) # G


def find_first_repeat_char(string):
    string = string.lower()
    occ = set()
    for char in string:
        if char in occ:
            return char

        occ.add(char)

    return None

# print(find_first_repeat_char('Green Apple')) # e


def most_frequent(nums):
    occ = {}
    for num in nums:
        if num not in occ:
            occ[num] = 1
        else:
            occ[num] += 1
    
    most_frequent = max(occ.values())
    for item in occ.keys():
        if occ[item] == most_frequent:
            return item

    return None

# print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  # 3


# ? HELPER METHOD
def binary_search(arr, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if x == arr[mid]:
            return (mid)
        elif(x > arr[mid]):
            return binary_search(arr, (mid + 1), high, x)
        else:
            return binary_search(arr, low, (mid -1), x)

    return -1


def count_pairs_with_diff(nums, k):
    pairs = 0
    nums = list(set(sorted(nums)))
    
    for i in range(len(nums) - 2):
        if binary_search(nums, i + 1, len(nums) - 1, nums[i] + k) != -1:
            pairs += 1

    return pairs


# 4 | HINT: Pairs: (1, 3) (3, 5) (5, 7) (7, 9)
# print(count_pairs_with_diff([1, 7, 5, 9, 2, 12, 3, 1], 2))


def two_sum(nums, target):
    hash_table = {}
    for i, num in enumerate(nums):
        print(hash_table)
        remainder = target - num
        if remainder in hash_table:
            return [hash_table[remainder], i]
        else:
            hash_table[num] = i
    return -1


print(two_sum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
print(two_sum(nums=[3, 2, 4], target=6))  # [1, 2]
print(two_sum(nums=[3, 3], target=6))  # [0, 1]
print(two_sum(nums=[-1, -2, -3, -4, -5], target=-8))  # [2, 4]
