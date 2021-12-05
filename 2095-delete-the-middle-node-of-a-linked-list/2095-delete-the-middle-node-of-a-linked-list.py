# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while (curr != None):
            length += 1
            curr = curr.next
        
        if length == 1:
            return None
        
        curr = head
        for i in range(0, length // 2 - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head
        