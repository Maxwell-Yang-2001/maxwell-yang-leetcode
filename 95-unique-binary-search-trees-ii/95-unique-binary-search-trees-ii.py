# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTreesWithList(list(range(1, n + 1)), 0, n)
    
    def generateTreesWithList(self, l: List[int], start: int, end: int) -> List[Optional[TreeNode]]:
        if start == end:
            return [None]
        else:
            result = []
            for i, n in enumerate(l[start : end]):
                leftList = self.generateTreesWithList(l, start, start + i)
                rightList = self.generateTreesWithList(l, start + i + 1, end)
                
                # combine all possibilities
                for leftNode in leftList:
                    for rightNode in rightList:
                        result.append(TreeNode(n, leftNode, rightNode))
            return result