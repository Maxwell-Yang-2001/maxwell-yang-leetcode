class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # use the hint: abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B).
        v0, v1, v2, v3 = [], [], [], []
        
        for i in range(len(arr1)):
            v0.append(arr1[i] + arr2[i] + i)
            v1.append(arr1[i] - arr2[i] - i)
            v2.append(arr1[i] + arr2[i] - i)
            v3.append(arr1[i] - arr2[i] + i)
            
        return max(max(v0) - min(v0), max(v1) - min(v1), max(v2) - min(v2), max(v3) - min(v3))
        
        