def shift_zeroes_to_the_end(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

nums = [int(num) for num in input().strip().split()]
shift_zeroes_to_the_end(nums)
print(nums)