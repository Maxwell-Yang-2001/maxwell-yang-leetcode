# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        # height: leave node has a height of 0
        def recurse(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            
            left_child_height = recurse(root.left)
            right_child_height = recurse(root.right)
            root_height = max(left_child_height, right_child_height) + 1
            
            if len(result) <= root_height:
                result.append([root.val])
            else:
                result[root_height].append(root.val)
            
            return root_height
        
        recurse(root)
        return result
            
                