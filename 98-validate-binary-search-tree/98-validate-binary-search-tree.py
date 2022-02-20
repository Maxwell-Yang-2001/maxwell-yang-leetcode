# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not root:
                return True
            
            if root.val > upper or root.val < lower:
                return False
            
            return valid(root.left, lower, root.val - 1) and valid(root.right, root.val + 1, upper)
            
        return valid(root, -2**31, 2**31 - 1)