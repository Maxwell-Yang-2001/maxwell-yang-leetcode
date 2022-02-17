class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target + 1)]
        dp[0].append([])
        
        for candidate in candidates:
            for s in range(candidate, target + 1):
                for prev in dp[s - candidate]:
                    new_list = prev.copy()
                    new_list.append(candidate)
                    dp[s].append(new_list)
        
        return dp[target]