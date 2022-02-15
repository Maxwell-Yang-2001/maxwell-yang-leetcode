class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > 26 or k > len(s):
            return 0
        freq = defaultdict(lambda:0)
        repeat = 0
        for c in s[:k]:
            freq[c] += 1
            if freq[c] == 2:
                repeat += 1
        
        result = 0
        if repeat == 0:
            result += 1
        
        for i in range(k, len(s)):
            freq[s[i-k]] -= 1
            if freq[s[i-k]] == 1:
                repeat -= 1
            freq[s[i]] += 1
            if freq[s[i]] == 2:
                repeat += 1
            if repeat == 0:
                result += 1

        return result