class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort so if a covers b, a comes before b in iterations
        intervals.sort(key=lambda n:n[0] * 100000 - n[1])
        prev = intervals[0]
        
        # first one is covered by first one, so + 1
        result = len(intervals) + 1
        
        for interval in intervals:
            if interval[0] >= prev[0] and interval[1] <= prev[1]:
                result -= 1
            else:
                prev = interval
        
        return result