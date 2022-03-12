"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node_dict = dict()
        curr = head
        while curr:
            node_dict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            curr_copy = node_dict[curr]
            if curr.next:
                curr_copy.next = node_dict[curr.next]
            if curr.random:
                curr_copy.random = node_dict[curr.random]
            curr = curr.next
        
        return node_dict[head]