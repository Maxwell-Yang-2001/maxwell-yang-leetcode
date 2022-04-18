# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        stack = []
        curr = root
        sentinel = TreeNode(-1)
        curr_parent = sentinel
        
        while curr != None:
            stack.append(curr)
            curr = curr.left
        
        while stack:
            curr = stack.pop()
            curr_parent.left = None
            curr_parent.right = curr
            curr_parent = curr
            curr = curr.right
            while curr != None:
                stack.append(curr)
                curr = curr.left
        
        curr_parent.left = None
        curr_parent.right = None
        return sentinel.right
            