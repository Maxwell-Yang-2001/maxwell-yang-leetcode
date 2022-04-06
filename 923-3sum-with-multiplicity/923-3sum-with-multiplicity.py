class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq = [0] * 101
        
        for i in arr:
            freq[i] += 1
        
        result = 0
        
        for y in range(101):
            # all diff
            for z in range(y + 1, 101):
                x = target - y - z
                if 0 <= x < y:
                    result += freq[x] * freq[y] * freq[z]
        
            other = target - 2 * y
            if 0 <= other <= 100:
                if other == y:
                    # 3 equal
                    result += freq[y] * (freq[y] - 1) * (freq[y] - 2) // 6
                else:
                    # 2 equal
                    result += freq[y] * (freq[y] - 1) // 2 * freq[other]
        
        return result % (10**9 + 7)