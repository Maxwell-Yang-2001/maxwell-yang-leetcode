class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for mid in range(len(s)):
            # check palindrome if mid is middle
            bestOffset = 0
            for offset in range(1, min(len(s) - mid, mid + 1)):
                if s[mid - offset] != s[mid + offset]:
                    break
                bestOffset = offset
            if (bestOffset * 2 + 1 > len(result)):
                result = s[mid-bestOffset : mid+bestOffset+1]
            # check palindrome if mid and mid + 1 are the middle
            bestOffset = -1
            for offset in range(0, min(len(s) - mid - 1, mid + 1)):
                if s[mid - offset] != s[mid + 1 + offset]:
                    break
                bestOffset = offset
            if bestOffset * 2 + 2 > len(result):
                result = s[mid-bestOffset: mid+bestOffset+2]
        return result