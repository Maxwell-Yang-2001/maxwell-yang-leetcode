# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        # in order traversal
        result = []
        toDo = deque([root, None]) # None is the end of current level
        while toDo:
            curr = toDo.popleft()
            if toDo and toDo[0] == None: # reaching the end of current level
                result.append(curr.val)
                toDo.popleft()
                if curr.left:
                    toDo.append(curr.left)
                if curr.right:
                    toDo.append(curr.right)
                if toDo:
                    toDo.append(None)
            else:
                if curr.left:
                    toDo.append(curr.left)
                if curr.right:
                    toDo.append(curr.right)
                
        
        return result
    
                