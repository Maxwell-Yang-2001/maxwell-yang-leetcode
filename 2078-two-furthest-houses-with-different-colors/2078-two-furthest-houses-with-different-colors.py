class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        best = 0
        
        for i, c in enumerate(colors):
            for j in range(len(colors) - 1, i, -1):
                if colors[j] != c:
                    best = max(best, j - i)
                    break
        
        return best
        