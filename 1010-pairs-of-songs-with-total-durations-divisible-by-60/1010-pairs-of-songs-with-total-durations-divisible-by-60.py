class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        occur = dict()
        for i in range(60):
            occur[i] = 0
        
        for song in time:
            song %= 60
            if song in occur:
                occur[song] += 1
        
        result = occur[30] * (occur[30] - 1) // 2 + occur[0] * (occur[0] - 1) // 2
        for i in range(1, 30):
            result += occur[i] * occur[60 - i]
        
        return result
            