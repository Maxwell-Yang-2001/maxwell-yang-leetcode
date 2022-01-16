class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # dynamic programming from the end
        l = len(arr)
        dp = [0] * l
        dp[l - 1] = arr[l - 1]
        
        for i in reversed(range(l - 1)):
            largest = 0
            best_sum = 0
            # position of splitting (between j and j + 1)
            for j in range(i, min(i + k, l)):
                largest = max(arr[j], largest)
                best_sum = max(largest * (j - i + 1) + (dp[j + 1] if j + 1 < l else 0), best_sum)
            
            dp[i] = best_sum

        return dp[0]