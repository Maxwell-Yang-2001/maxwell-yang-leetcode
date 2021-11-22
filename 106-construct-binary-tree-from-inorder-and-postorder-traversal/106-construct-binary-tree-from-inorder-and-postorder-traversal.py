# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeRecu(inorder, 0, postorder, 0, len(postorder) - 1)
    
    def buildTreeRecu(self, inorder: List[int], inStart: int, postorder: List[int], postStart: int, width: int) -> Optional[TreeNode]:
        if width < 0:
            return None
        
        rootVal = postorder[postStart + width]
        
        # cannot binary search as this is not sorted
        rootIndexInInorder = inStart
        while (inorder[rootIndexInInorder] != rootVal):
            rootIndexInInorder += 1
        
        left = self.buildTreeRecu(inorder, inStart, postorder, postStart, rootIndexInInorder - inStart - 1)
        right = self.buildTreeRecu(inorder, rootIndexInInorder + 1, postorder, rootIndexInInorder - inStart + postStart, inStart + width - rootIndexInInorder - 1)
        
        return TreeNode(rootVal, left, right)