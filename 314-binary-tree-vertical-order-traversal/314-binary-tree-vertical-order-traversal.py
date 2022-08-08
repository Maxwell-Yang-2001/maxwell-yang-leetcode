# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        # inorder traversal with position value
        # we know for sure that the result would be contiguous in index, since BFS would span index + 1 / - 1 to children
        # we call root at index 0, its left and right child at index -1 and +1, and start inorder traversal
        collected = defaultdict(lambda: [])
        
        to_visit = deque([(root, 0)])
        while to_visit:
            curr, index = to_visit.popleft()
            if curr == None:
                continue
            else:
                collected[index].append(curr.val)
                to_visit.append((curr.left, index - 1))
                to_visit.append((curr.right, index + 1))
            
        indices = list(collected)
        result = []
        for i in range(min(indices), max(indices) + 1):
            result.append(collected[i])
        
        return result
            
                
            