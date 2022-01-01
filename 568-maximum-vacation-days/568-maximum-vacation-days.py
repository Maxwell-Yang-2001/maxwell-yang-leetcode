class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        cityCount = len(days)
        weekCount = len(days[0])
        best = [[0] * weekCount for i in range(cityCount)]
        
        connections = dict()
        # set up adjancency list (include the city itself in case of staying)
        for city in range(cityCount):
            connections[city] = [city]
        
        for src, flight in enumerate(flights):
            for dst, hasFlight in enumerate(flight):
                if hasFlight == 1:
                    connections[src].append(dst)
        
        # set up last week
        for city in range(cityCount):
            best[city][weekCount - 1] = days[city][weekCount - 1]
        
        # go from second to last week to first week
        for week in range(weekCount - 2, -1, -1):
            for city in range(cityCount):
                maxDays = 0
                for dst in connections[city]:
                    maxDays = max(maxDays, best[dst][week + 1])
                best[city][week] = maxDays + days[city][week]
        
        maxDays = 0
        for dst in connections[0]:
            maxDays = max(maxDays, best[dst][0])
        
        return maxDays