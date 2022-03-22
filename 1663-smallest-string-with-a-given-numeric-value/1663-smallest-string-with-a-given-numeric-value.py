class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ord_diff = ord('a') - 1
        result = ['0' for i in range(n)]
        for pos in range(n - 1, -1, -1):
            add = min(k - pos, 26)
            result[pos] = chr(add + ord_diff)
            k -= add
        return ''.join(result)