# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        tup = self.plusOneRecu(head)
        if tup[1]:
            return ListNode(1, tup[0])
        return tup[0]
    
    def plusOneRecu(self, head: Optional[ListNode]) -> tuple[Optional[ListNode], bool]:
        if head == None:
            return [None, True]
        else:
            nextTuple = self.plusOneRecu(head.next)
            head.next = nextTuple[0]
            if nextTuple[1]:
                head.val += 1
            if head.val == 10:
                head.val = 0
                return [head, True]
            return [head, False]