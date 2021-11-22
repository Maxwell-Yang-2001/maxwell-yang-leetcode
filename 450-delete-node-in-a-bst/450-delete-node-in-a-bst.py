# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        targetTuple = self.findNode(root, key)
        target = targetTuple[0]
        targetParent = targetTuple[1]
        if target == None:
            return root
        
        if target.left != None:
            target.val = target.left.val
            if target.right == None:
                target.right = target.left.right
            else:
                self.insertMost(target.right, target.left.right, True)
            target.left = target.left.left    
        elif target.right != None:
            target.val = target.right.val
            if target.left == None:
                target.left = target.right.left
            else:
                self.insertMost(target.left, target.right.left, False)
            target.right = target.right.right
        else:
            # meaning we are at root
            if targetParent == None:
                return None
            else:
                if targetParent.left == target:
                    targetParent.left = None
                else:
                    targetParent.right = None

        return root
        
    def findNode(self, root: Optional[TreeNode], key: int) -> tuple[Optional[TreeNode], Optional[TreeNode]]:
        if root == None:
            return [None, None]
        elif root.val == key:
            return [root, None]
        elif root.val < key:
            tup = self.findNode(root.right, key)
            if tup[1] == None:
                tup[1] = root
            return tup
        else:
            tup = self.findNode(root.left, key)
            if tup[1] == None:
                tup[1] = root
            return tup
    
    def insertMost(self, root: TreeNode, toInsert: TreeNode, left: bool) -> None:
        if left:
            if root.left == None:
                root.left = toInsert
            else:
                self.insertMost(root.left, toInsert, True)
        else:
            if root.right == None:
                root.right = toInsert
            else:
                self.insertMost(root.right, toInsert, True)