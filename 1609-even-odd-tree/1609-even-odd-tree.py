# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # use None to indicate the end of one level
        queue = [root, None]
        prevVal = -1
        currLvlOdd = True
        while len(queue) != 0:
            curr = queue.pop(0)
            if curr == None:
                if (len(queue) == 0):
                    return True
                queue.append(None)
                currLvlOdd = not currLvlOdd
                prevVal = -1 if currLvlOdd else 1000002
            else:
                currVal = curr.val
                if currLvlOdd:
                    if currVal % 2 == 0 or prevVal >= currVal:
                        return False
                else:
                    if currVal % 2 == 1 or prevVal <= currVal:
                        return False
                prevVal = currVal
                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)
        return True
                
        