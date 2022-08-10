# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def gen(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            else:
                mid = (start + end) // 2
                return TreeNode(nums[mid], gen(start, mid - 1), gen(mid + 1, end))
        return gen(0, len(nums) - 1)
    
            
                