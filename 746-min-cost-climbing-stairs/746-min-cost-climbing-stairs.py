class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        prev = 0 # min cost to previous stair
        curr = 0 # min cost to current stair
        for i in range(2, len(cost)):
            new = min(prev + cost[i - 2], curr + cost[i - 1])
            prev = curr
            curr = new
        
        return curr