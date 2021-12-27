class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = 0
        for n in arr:
            s += n
        if s % 3 != 0:
            return False
        s //= 3
        
        startI = 0
        for rounds in range(2):
            currS = 0
            reached = False
            for i in range(startI, len(arr)):
                currS += arr[i]
                if currS == s:
                    reached = True
                    startI = i + 1
                    break
            if not reached:
                return False
        
        return startI != len(arr)
            