# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.sumRecur(root, 0)
    def sumRecur(self, root: Optional[TreeNode], sumSoFar: int) -> int:
        if root == None:
            return -1
        
        sumSoFar = sumSoFar * 2 + root.val
        lSum = self.sumRecur(root.left, sumSoFar)
        rSum = self.sumRecur(root.right, sumSoFar)
        
        if lSum == -1:
            if rSum == -1:
                return sumSoFar
            else:
                return rSum
        else:
            if rSum == -1:
                return lSum
            else:
                return lSum + rSum