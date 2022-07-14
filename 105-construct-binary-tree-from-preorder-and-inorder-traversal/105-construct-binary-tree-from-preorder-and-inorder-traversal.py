# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recursive(pre_ends: (int, int), in_ends: (int, int)) -> Optional[TreeNode]:
            pre_left, pre_right = pre_ends
            in_left, in_right = in_ends
            if pre_left >= pre_right:
                return None
            
            root_val = preorder[pre_left]
            root_pos = inorder.index(root_val, in_left, in_right)
            
            left_len = root_pos - in_left
            right_len = in_right - root_pos - 1
            
            left_child = recursive((pre_left + 1, pre_left + left_len + 1), (in_left, root_pos))
            right_child = recursive((pre_right - right_len, pre_right), (root_pos + 1, in_right))
            return TreeNode(root_val, left_child, right_child)
        
        return recursive((0, len(preorder)), (0, len(inorder)))