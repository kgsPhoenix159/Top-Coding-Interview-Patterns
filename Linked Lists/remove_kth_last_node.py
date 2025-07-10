class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def remove_kth_last_node(head, k):
    dummy = ListNode(-1)
    dummy.next = head

    trailer = leader = dummy
    
    for _ in range(k):
        leader = leader.next

        if not leader:
            return head
    
    while leader.next:
        leader = leader.next
        trailer = trailer.next
    
    trailer.next = trailer.next.next

    return dummy.next

nums = [int(num) for num in input().strip().split(" -> ")]
k = int(input().strip())

def list_to_linked_list(nums):
    if not nums:
        return None
    
    head = ListNode(nums[0])
    current = head

    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    
    return head

list_after_removing_kth_last_node = remove_kth_last_node(list_to_linked_list(nums), k)

while list_after_removing_kth_last_node.next:
    print("{} -> ".format(list_after_removing_kth_last_node.value), end="")
    list_after_removing_kth_last_node = list_after_removing_kth_last_node.next
print(list_after_removing_kth_last_node.value)