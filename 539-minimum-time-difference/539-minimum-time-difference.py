class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = set()
        for timePoint in timePoints:
            time = int(timePoint[0:2]) * 60 + int(timePoint[-2:])
            if time in times:
                return 0
            times.add(time)
        
        timeList = list(times)
        timeList.sort()
        
        timeLen = len(timeList)
        minInDay = 1440
        diff = timeList[timeLen - 1] - timeList[0]
        minDiff = min(diff, minInDay - diff)
        for i in range(timeLen - 1):
            diff = timeList[i + 1] - timeList[i]
            minDiff = min(minDiff, diff, minInDay - diff)
        
        return minDiff