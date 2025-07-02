def longest_chain_of_consecutive_numbers(nums):
    if not nums:
        return 0
    
    nums_set = set(nums)
    longest_chain = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_chain = 1

            while current_num + 1 in nums_set:
                current_chain += 1
                current_num += 1
            
            longest_chain = max(longest_chain, current_chain)
    
    return longest_chain

nums = [int(num) for num in input().strip().split()]
longest_consecutive_chain = longest_chain_of_consecutive_numbers(nums)
print(longest_consecutive_chain)