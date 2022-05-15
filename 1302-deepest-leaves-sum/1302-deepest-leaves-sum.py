# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deepest_level = 0
        curr_sum = 0
        def traverse(node: TreeNode, level: int):
            nonlocal deepest_level
            nonlocal curr_sum
            if not node.left and not node.right:
                if level == deepest_level:
                    curr_sum += node.val
                elif level > deepest_level:
                    curr_sum = node.val
                    deepest_level = level
                    
            else:
                if node.left:
                    traverse(node.left, level + 1)
                if node.right:
                    traverse(node.right, level + 1)
        traverse(root, 0)
        return curr_sum