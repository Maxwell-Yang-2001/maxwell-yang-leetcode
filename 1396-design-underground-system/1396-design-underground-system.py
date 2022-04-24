class UndergroundSystem:
    
    def __init__(self):
        self.customers = dict()
        self.records = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prevStation, prevTime = self.customers[id]
        del self.customers[id]
        if not prevStation in self.records:
            self.records[prevStation] = dict()
        group = self.records[prevStation]
        if not stationName in group:
            group[stationName] = (0, 0)
        prevSum, prevCount = group[stationName]
        group[stationName] = (prevSum + t - prevTime, prevCount + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        record = self.records[startStation][endStation]
        return record[0] / record[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)