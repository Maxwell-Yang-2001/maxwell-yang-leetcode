# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        result = curr = ListNode(0)
        q = PriorityQueue()
        
        # put lists into priorityQueue
        for l in lists:
            if l != None:
                q.put(Wrapper(l))
        
        while not q.empty():
            l = q.get().node
            n = ListNode(l.val)
            curr.next = n
            curr = n
            if l.next:
                q.put(Wrapper(l.next))
            
        return result.next