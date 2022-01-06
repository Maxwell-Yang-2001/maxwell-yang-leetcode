# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        occur = dict()
        
        curr = head
        while curr != None:
            currVal = curr.val
            if currVal in occur:
                occur[currVal] += 1
            else:
                occur[currVal] = 1
            curr = curr.next
        
        for num in list(occur):
            if occur[num] == 1:
                del occur[num]
        
        return self.deleteDupRecur(head, set(occur))
        
    def deleteDupRecur(self, head: ListNode, occur: dict[int, int]) -> ListNode:
        if head == None:
            return None
        
        if head.val in occur:
            return self.deleteDupRecur(head.next, occur)
        
        head.next = self.deleteDupRecur(head.next, occur)
        return head
        
        
        