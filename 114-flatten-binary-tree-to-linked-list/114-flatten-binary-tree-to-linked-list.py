# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def recurse(root: Optional[TreeNode]) -> (Optional[TreeNode], Optional[TreeNode]):
            if not root:
                return (None, None)
            
            left_head, left_tail = recurse(root.left)
            right_head, right_tail = recurse(root.right)
            
            root.left = None
            
            if left_head:
                root.right = left_head
                if right_head:
                    left_tail.right = right_head
                    return (root, right_tail)
                else:
                    return (root, left_tail)
            elif right_head:
                root.right = right_head
                return (root, right_tail)
            else:
                return (root, root)
        
        recurse(root)