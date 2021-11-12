class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, best = 0, 0, 0
        seen = set()
        while end != len(s):
            tail = s[end]
            if tail in seen:
                while start != end:
                    head = s[start]
                    seen.remove(head)
                    start += 1
                    if head == tail:
                        break
            seen.add(tail)
            best = max(best, end - start + 1)
            end += 1
        return best