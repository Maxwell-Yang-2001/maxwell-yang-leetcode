"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        node_list = [None] * 101
        edges = [set() for i in range(101)]
        
        # BFS
        to_do = deque([node])
        
        while to_do:
            curr_node = to_do.popleft()
            curr_val = curr_node.val
            copied_curr = node_list[curr_val]
            
            if not copied_curr:
                copied_curr = node_list[curr_val] = Node(curr_val, [])
                
            for neighbor_node in curr_node.neighbors:
                neighbor_val = neighbor_node.val
                smaller_val, larger_val = min(curr_val, neighbor_val), max(curr_val, neighbor_val)
                
                # have considered this edge, skip
                if larger_val in edges[smaller_val]:
                    continue
                
                edges[smaller_val].add(larger_val)
                copied_neighbor = node_list[neighbor_val]
                if not copied_neighbor:
                    copied_neighbor = node_list[neighbor_val] = Node(neighbor_val, [])
                    to_do.append(neighbor_node)
                
                copied_neighbor.neighbors.append(copied_curr)
                copied_curr.neighbors.append(copied_neighbor)
        
        return node_list[node.val]