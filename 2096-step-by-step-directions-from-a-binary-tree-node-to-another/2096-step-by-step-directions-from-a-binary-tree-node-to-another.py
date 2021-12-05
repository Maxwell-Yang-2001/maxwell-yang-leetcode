# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pathToStart = []
        pathToDest = []
        self.dfs(root, startValue, destValue, 0, pathToStart, pathToDest)
        pathToStart.pop(0)
        pathToDest.pop(0)
        shareEndIndex = 0
        while shareEndIndex < len(pathToStart) and shareEndIndex < len(pathToDest) and pathToStart[shareEndIndex] == pathToDest[shareEndIndex]:
            shareEndIndex += 1
        
        result = []
        
        # append U until finding the common ancestor
        for i in range(len(pathToStart) - 1, shareEndIndex - 1, -1):
            result.append('U')
        
        # append how to go to dest from common ancestor
        for i in range(shareEndIndex, len(pathToDest)):
            result.append(pathToDest[i])
        
        return ''.join(result)
        
        
    
    def dfs(self, root: Optional[TreeNode], startValue: int, destValue: int, level: int, pathToStart: List[str], pathToDest: List[str]) -> None:
        if root == None:
            return
        
        if root.val == startValue:
            pathToStart.append('')
            for i in range(level):
                pathToStart.append(path[i])
            if len(pathToDest) != 0:
                return
                
        elif root.val == destValue:
            pathToDest.append('')
            for i in range(level):
                pathToDest.append(path[i])
            if len(pathToStart) != 0:
                return
            
        # go left
        if len(path) <= level:
            path.append('L')
        else:
            path[level] = 'L'
        self.dfs(root.left, startValue, destValue, level + 1, pathToStart, pathToDest)
        if len(pathToStart) != 0 and len(pathToDest) != 0:
            return
            
        # go right
        path[level] = 'R'
        self.dfs(root.right, startValue, destValue, level + 1, pathToStart, pathToDest)