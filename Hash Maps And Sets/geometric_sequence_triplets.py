from collections import defaultdict

def geometric_sequence_triplets(nums, r):
    left_heap = defaultdict(int)
    right_heap = defaultdict(int)
    count = 0
    for num in nums:
        right_heap[num] += 1
    for num in nums:
        right_heap[num] -= 1
        if num % r == 0:
            count += left_heap[num // r] * right_heap[num * r]
        left_heap[num] += 1
    return count

nums = [int(num) for num in input().strip().split()]
r = int(input().strip())
freqs = geometric_sequence_triplets(nums, r)
print(freqs)