# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        
        # BFS, but using None to indicate between levels
        toDo = [root, None]
        found = False
        while len(toDo) > 0:
            curr = toDo.pop(0)
            if curr != None:
                # we are at the end of current level
                if curr == u:
                    found = True
                    break
                if curr.left != None:
                    toDo.append(curr.left)
                if curr.right != None:
                    toDo.append(curr.right)
                if toDo[0] == None:
                    toDo.append(None)
        
        if found and len(toDo) > 0:
            # this would be None if u is the last element in the level, or the nearest next one otherwise
            return toDo[0]
        
        return None