class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        l = len(arr)
        step = (arr[l - 1] - arr[0]) // l
        for i in range(l - 1):
            if arr[i + 1] - arr[i] != step:
                return arr[i] + step
        
        # if step is 0:
        return arr[0]