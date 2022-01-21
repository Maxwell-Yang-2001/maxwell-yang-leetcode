class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, curr_tank, start = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        
        return start if tank >= 0 else -1
        
        