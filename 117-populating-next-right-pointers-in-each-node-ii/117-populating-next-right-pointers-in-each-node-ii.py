"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # just BFS, None indicates end of a level
        if not root:
            return root
        todo = deque([root, None])
        prev = None
        while todo:
            curr = todo.popleft()
            if prev:
                prev.next = curr
            if not curr:
                if todo:
                    todo.append(None)
            else:
                if curr.left:
                    todo.append(curr.left)
                if curr.right:
                    todo.append(curr.right)
            prev = curr
        return root
                
                