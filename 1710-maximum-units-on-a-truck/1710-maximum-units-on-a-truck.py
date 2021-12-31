class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda boxType:boxType[1], reverse=True)
        unitTotal = 0
        for bt in boxTypes:
            numBoxes = min(truckSize, bt[0])
            unitTotal += numBoxes * bt[1]
            truckSize -= numBoxes
            if truckSize == 0:
                break
        return unitTotal
            