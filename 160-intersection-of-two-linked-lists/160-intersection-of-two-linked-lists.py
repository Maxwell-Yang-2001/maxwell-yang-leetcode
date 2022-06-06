# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLen(head: ListNode) -> int:
            result = 0
            while head:
                result += 1
                head = head.next
            return result
        len_a, len_b = getLen(headA), getLen(headB)
        if len_a < len_b:
            len_a, len_b = len_b, len_a
            headA, headB = headB, headA
        diff = len_a - len_b
        for i in range(diff):
            headA = headA.next
        
        # now both heads are at same length
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
            