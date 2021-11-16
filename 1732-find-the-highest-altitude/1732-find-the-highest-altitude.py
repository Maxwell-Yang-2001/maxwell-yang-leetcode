class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        best, sum = 0, 0
        for g in gain:
            sum += g
            if best < sum:
                best = sum
        return best