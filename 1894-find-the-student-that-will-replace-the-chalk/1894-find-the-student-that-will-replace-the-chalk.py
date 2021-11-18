class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum = 0
        for c in chalk:
            sum += c
        
        k = k % sum
        
        for i, c in enumerate(chalk):
            k -= c
            if k < 0:
                return i
        return -1