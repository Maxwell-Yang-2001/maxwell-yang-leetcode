class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = math.floor(len(arr) / 4) + 1
        freq = dict()
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            if freq[i] == target:
                return i
        return -1
        