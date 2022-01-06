class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = dict()
        
        for trip in trips:
            if trip[1] in stops:
                stops[trip[1]] += trip[0]
            else:
                stops[trip[1]] = trip[0]
            
            if trip[2] in stops:
                stops[trip[2]] -= trip[0]
            else:
                stops[trip[2]] = -trip[0]
        
        stopList = list(stops)
        stopList.sort()
        
        peopleCount = 0
        for stop in stopList:
            peopleCount += stops[stop]
            if peopleCount > capacity:
                return False
        
        return True
        
        