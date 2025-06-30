def pair_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            return [left, right]
    return []

nums = [int(num) for num in input().strip().split()]
target = int(input().strip())
indices = pair_sum_sorted(nums, target)
print(indices)