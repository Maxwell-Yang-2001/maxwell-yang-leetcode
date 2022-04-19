# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = []
        curr = root
        while curr:
            stack.append(curr)
            curr = curr.left
        
        small, large = None, None
        prev = None
        while stack:
            curr = stack.pop()
            if prev and prev.val > curr.val:
                small = curr
                if not large:
                    large = prev
                else:
                    break
            prev = curr
            curr = curr.right
            while curr:
                stack.append(curr)
                curr = curr.left

        # swap!
        tmp = small.val
        small.val = large.val
        large.val = tmp