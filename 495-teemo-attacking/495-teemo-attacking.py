class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # last one always last for duration
        result = duration
        for i in range(len(timeSeries) - 1):
            result += min(duration, timeSeries[i + 1] - timeSeries[i])
        
        return result