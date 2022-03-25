class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda p: p[0] - p[1])
        
        result = 0
        half = len(costs) // 2
        for i in range(half):
            result += costs[i][0] + costs[i + half][1]
        
        return result