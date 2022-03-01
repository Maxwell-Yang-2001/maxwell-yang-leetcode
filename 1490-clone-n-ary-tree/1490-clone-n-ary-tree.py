"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        root = Node(node.val)
        
        toDo = deque([(node, root)])
        
        while toDo:
            orig, curr = toDo.popleft()
            for orig_child in orig.children:
                curr_child = Node(orig_child.val)
                curr.children.append(curr_child)
                toDo.append((orig_child, curr_child))
        
        return root