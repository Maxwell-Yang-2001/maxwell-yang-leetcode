class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = []
        for i, row in enumerate(mat):
            count = 0
            for j in row:
                count += j
            l.append((i, count))
        
        l.sort(key = lambda entry: entry[1])
        
        result = []
        for i in range(k):
            result.append(l[i][0])
        
        return result