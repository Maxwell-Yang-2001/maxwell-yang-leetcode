class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1
        
        for ele in arr:
            if ele == curr:
                curr += 1
                continue
            else:
                k -= (ele - curr)
                if k <= 0:
                    return ele + k - 1
                curr = ele + 1
        return curr + k - 1