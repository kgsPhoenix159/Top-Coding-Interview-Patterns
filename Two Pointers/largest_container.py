def largest_container(heights):
    maxm_amount = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        maxm_amount = max(min(heights[left], heights[right]) * (right - left), maxm_amount)
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return maxm_amount

heights = [int(height) for height in input().strip().split()]
maximum_amount = largest_container(heights)
print(maximum_amount)