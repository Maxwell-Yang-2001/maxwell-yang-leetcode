# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        toDo = [root]
        while(len(toDo) != 0):
            curr = toDo.pop(0)
            if curr.left == None:
                if curr.right != None:
                    result.append(curr.right.val)
                    toDo.append(curr.right)
            else:
                toDo.append(curr.left)
                if curr.right != None:
                    toDo.append(curr.right)
                else:
                    result.append(curr.left.val)
        return result
                