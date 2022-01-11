"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pPath = []
        qPath = []
        while p != None:
            pPath.append(p)
            p = p.parent
        
        while q != None:
            qPath.append(q)
            q = q.parent
        
        lenP = len(pPath)
        lenQ = len(qPath)
        
        for i in range(min(lenP, lenQ)):
            if pPath[lenP - 1 - i] != qPath[lenQ - 1 - i]:
                return pPath[lenP - i]
        
        return qPath[0] if lenP > lenQ else pPath[0]
        
                
        
        