def triplet_sum(nums):
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        a = -nums[i]
        b = i + 1
        c = len(nums) - 1
        while b < c:
            curr_sum = nums[b] + nums[c]
            if curr_sum < a:
                b += 1
            elif curr_sum > a:
                c -= 1
            else:
                triplets.append([nums[i], nums[b], nums[c]])
                b += 1
                while b < c and nums[b] == nums[b - 1]:
                    b += 1
    return triplets

nums = [int(num) for num in input().strip().split()]
triplets_with_sum_equal_to_zero = triplet_sum(nums)
print(triplets_with_sum_equal_to_zero)