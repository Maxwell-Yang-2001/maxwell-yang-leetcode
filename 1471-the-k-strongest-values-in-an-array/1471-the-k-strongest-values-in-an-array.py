class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arrCopy = copy.deepcopy(arr)
        arrCopy.sort()
        median = arrCopy[(len(arr) - 1) // 2]
        
        pairArr = []
        for i, n in enumerate(arr):
            pairArr.append((abs(n - median), n))
        pairArr.sort(reverse=True)
        
        result = [0] * k 
        for i in range(k):
            result[i] = pairArr[i][1]
        
        return result
            