# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # we just need to find the path, so use DFS for now
        def dfs(root: TreeNode, val: int) -> TreeNode:
            if root.val == val:
                return root
            elif not (root.left or root.right):
                return None
            else:
                result = None
                if root.left:
                    result = dfs(root.left, val)
                if not result and root.right:
                    result = dfs(root.right, val)
                return result
        return dfs(cloned, target.val)