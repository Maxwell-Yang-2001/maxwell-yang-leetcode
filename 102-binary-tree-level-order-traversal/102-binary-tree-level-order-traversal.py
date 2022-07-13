# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        to_visit = deque([root, None]) # None sentinel indicates end of current level
        
        result = []
        curr_level = []
        
        while to_visit:
            curr = to_visit.popleft()
            curr_level.append(curr.val)
            if curr.left:
                to_visit.append(curr.left)
            if curr.right:
                to_visit.append(curr.right)
            if to_visit and to_visit[0] == None:
                to_visit.popleft()
                if to_visit:
                    to_visit.append(None)
                result.append(curr_level)
                curr_level = []
        
        return result