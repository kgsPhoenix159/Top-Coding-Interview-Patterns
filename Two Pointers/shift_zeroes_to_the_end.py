def shift_zeroes_to_the_end(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

nums = [int(num) for num in input().strip().split()]
shift_zeroes_to_the_end(nums)
print(nums)