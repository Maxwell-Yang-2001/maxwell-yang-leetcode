class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, best = 0, 0, 0
        seen = {}
        while end != len(s):
            curr = s[end]
            if curr in seen and start <= seen[curr]:
                start = seen[curr] + 1
            seen[curr] = end
            best = max(best, end - start + 1)
            end += 1
        return best