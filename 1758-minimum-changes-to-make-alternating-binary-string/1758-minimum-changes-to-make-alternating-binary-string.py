class Solution:
    def minOperations(self, s: str) -> int:
        # we count the number to make it alternate starting with 0, and the other is just a complement
        count = 0
        for i, c in enumerate(s):
            if c == "1":
                if i % 2 == 1:
                    count += 1
            elif i % 2 == 0:
                count += 1
        
        return min(count, len(s) - count)
                