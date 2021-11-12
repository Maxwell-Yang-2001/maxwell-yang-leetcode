# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head:
            next = self.removeElements(head.next, val)
            if head.val == val:
                return next
            else:
                head.next = next
                return head
        else:
            return None