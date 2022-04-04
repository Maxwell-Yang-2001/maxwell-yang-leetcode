# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr != None:
            l += 1
            curr = curr.next
        
        toDo = [k - 1, l - k]
        toDo.sort()
        
        node1, node2 = None, None
        
        curr = head
        for i in range(toDo[1] + 1):
            if i == toDo[0]:
                node1 = curr
            if i == toDo[1]:
                node2 = curr
            curr = curr.next
        
        tmp = node1.val
        node1.val = node2.val
        node2.val = tmp
        
        return head
            