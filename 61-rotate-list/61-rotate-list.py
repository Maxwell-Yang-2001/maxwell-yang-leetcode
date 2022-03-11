# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        tail = head
        l = 0
        
        # get length of list
        while curr:
            l += 1
            tail = curr
            curr = curr.next
        
        k %= l
        if k == 0:
            return head
        
        new_tail = head
        
        k = l - 1 - k
        
        while k > 0:
            k -= 1
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        tail.next = head
        return new_head
        