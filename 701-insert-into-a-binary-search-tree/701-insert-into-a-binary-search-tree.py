# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val=val)
        self.insertRecur(root, val)
        return root
    
    # root is not none
    def insertRecur(self, root: TreeNode, val: int) -> None:
        # insert to left
        if root.val > val:
            if root.left == None:
                root.left = TreeNode(val=val)
            else:
                self.insertRecur(root.left, val)
        # insert to right
        else:
            if root.right == None:
                root.right = TreeNode(val=val)
            else:
                self.insertRecur(root.right, val)