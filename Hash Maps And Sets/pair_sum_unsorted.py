def pair_sum_unsorted(nums, target):
    nums_with_indices_heap = {}
    for i, num in enumerate(nums):
        if target - num in nums_with_indices_heap:
            return [nums_with_indices_heap[target - num], i]
        else:
            nums_with_indices_heap[num] = i
    return []

nums = [int(num) for num in input().strip().split()]
target = int(input().strip())
pair_of_indices = pair_sum_unsorted(nums, target)
print(pair_of_indices)