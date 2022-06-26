class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        if l == k:
            return sum(cardPoints)
        
        curr_sum = sum(cardPoints[:(l - k)])
        min_sum = curr_sum
        
        for i in range(l - k, l):
            curr_sum += (cardPoints[i] - cardPoints[i - (l - k)])
            min_sum = min(curr_sum, min_sum)
        
        return sum(cardPoints) - min_sum