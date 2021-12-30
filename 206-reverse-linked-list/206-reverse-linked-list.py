# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        return self.reverseListRecur(head)[0]
    
    def reverseListRecur(self, head: ListNode) -> (ListNode, ListNode):
        if head.next == None:
            return (head, head)
        
        recurResult = self.reverseListRecur(head.next)
        head.next = None
        recurResult[1].next = head
        return (recurResult[0], head)