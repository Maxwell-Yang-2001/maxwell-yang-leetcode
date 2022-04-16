# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        stack = []
        curr_sum = 0
        curr = root
        
        while curr:
            stack.append(curr)
            curr = curr.right

        while stack:
            curr = stack.pop()
            curr_sum += curr.val
            curr.val = curr_sum
            curr = curr.left
            while curr:
                stack.append(curr)
                curr = curr.right
        
        return root