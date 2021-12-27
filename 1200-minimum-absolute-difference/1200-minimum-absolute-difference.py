class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        minDiff = 10**7
        for i in range(len(arr) - 1):
            currDiff = arr[i + 1] - arr[i]
            if currDiff <= minDiff:
                if currDiff < minDiff:
                    result.clear()
                    minDiff = currDiff
                result.append((arr[i], arr[i + 1]))
        return result
                    