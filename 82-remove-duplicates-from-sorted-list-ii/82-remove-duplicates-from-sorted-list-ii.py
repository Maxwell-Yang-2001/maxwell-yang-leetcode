# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr_group_dup = False
        head = ListNode(-101, head)
        curr_group_start = head
        head = ListNode(-102, head)
        prev = head
        
        while curr:
            if curr.val == curr_group_start.val:
                curr_group_dup = True
            else:
                if curr_group_dup:
                    prev.next = curr
                else:
                    prev = prev.next
                curr_group_dup = False
                curr_group_start = curr 
                
            curr = curr.next
        
        if curr_group_dup:
            prev.next = None
        return head.next.next
        