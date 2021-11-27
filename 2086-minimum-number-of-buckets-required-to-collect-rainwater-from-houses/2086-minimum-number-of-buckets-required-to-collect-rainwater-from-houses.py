class Solution:
    def minimumBuckets(self, street: str) -> int:
        currEmptyCount = 0
        result = 0
        emptyList = []
        for c in street:
            if c == '.':
                currEmptyCount += 1
            else:
                emptyList.append(currEmptyCount)
                currEmptyCount = 0
        emptyList.append(currEmptyCount)
        
        # we use -1 in emptyList to indicate there is already a bucket
        for i in range(len(emptyList) - 1):
            if emptyList[i] == -1:
                continue
            if emptyList[i + 1] == 0:
                if emptyList[i] == 0:
                    return -1
            else:
                emptyList[i + 1] -= 1
                if emptyList[i + 1] == 0:
                    emptyList[i + 1] = -1
            result += 1
        
        return result
            
                    