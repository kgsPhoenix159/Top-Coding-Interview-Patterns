# Definition of ListNode:
class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def linked_list_reversal(head):
    curr_node = head
    prev_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    
    return prev_node

nums = [int(num) for num in input().strip().split(" -> ")]

def list_to_linked_list(nums):
    if not nums:
        return None
    
    head = ListNode(nums[0])
    current = head

    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    
    return head

reversed_linked_list = linked_list_reversal(list_to_linked_list(nums))

while reversed_linked_list.next != None:
    print("{} -> ".format(reversed_linked_list.value), end="")
    reversed_linked_list = reversed_linked_list.next
print(reversed_linked_list.value)