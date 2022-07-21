# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # sentinel head for cases that left = 1
        # get to right before left
        head = ListNode(0, head)
        before = head
        for i in range(1, left):
            before = before.next
        
        # inner_head and inner_tail is the head and tail of the middle changing part
        inner_head = inner_tail = before.next
        for i in range(left, right):
            new_inner_head = inner_tail.next
            inner_tail.next = new_inner_head.next
            new_inner_head.next = inner_head
            before.next = new_inner_head
            inner_head = new_inner_head
        
        return head.next
            