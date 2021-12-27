# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while len(stack) != 0:
            ele = stack.pop()
            if ele == None:
                continue
            result.append(ele.val)
            stack.append(ele.right)
            stack.append(ele.left)
        return result