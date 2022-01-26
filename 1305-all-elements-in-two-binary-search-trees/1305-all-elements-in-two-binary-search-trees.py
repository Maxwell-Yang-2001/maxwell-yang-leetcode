# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        q1, q2 = [], []
        curr1, curr2 = root1, root2
        result = []
            
        while q1 or q2 or curr1 or curr2:
            while curr1:
                q1.append(curr1)
                curr1 = curr1.left
                
            while curr2:
                q2.append(curr2)
                curr2 = curr2.left
            if q1 or curr1:
                if q2 or curr2:
                    # tree 1 and tree 2
                    val1 = curr1.val if curr1 else q1[-1].val
                    val2 = curr2.val if curr2 else q2[-1].val
                    if val1 <= val2:
                        curr1 = self.iterate(curr1, q1, result)
                    else:
                        curr2 = self.iterate(curr2, q2, result)
                else:
                    # tree 1 only
                    curr1 = self.iterate(curr1, q1, result)
            else:
                # tree 2 only
                curr2 = self.iterate(curr2, q2, result)
        
        return result
    def iterate(self, curr: TreeNode, queue: List[TreeNode], result: List[int]) -> TreeNode:
        while curr:
            queue.append(curr)
            curr = curr.left
        curr = queue.pop()
        result.append(curr.val)
        return curr.right