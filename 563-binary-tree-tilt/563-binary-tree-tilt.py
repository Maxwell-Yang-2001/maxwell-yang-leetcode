# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.findTiltAndSumAndSumTilts(root)[2]
    
    def findTiltAndSumAndSumTilts(self, root: Optional[TreeNode]) -> (int, int, int):
        if root == None:
            return (0, 0, 0)
        else:
            left = self.findTiltAndSumAndSumTilts(root.left)
            right = self.findTiltAndSumAndSumTilts(root.right)
            currTilt = abs(left[1] - right[1])
            return (currTilt, left[1] + right[1] + root.val, left[2] + right[2] + currTilt)