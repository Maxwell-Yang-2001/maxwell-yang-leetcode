class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(start: int, end: int) -> bool:
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        start = 0
        end = len(s) - 1
        # still have pairs to check
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return (s[start + 1] == s[end] and isPalindrome(start + 2, end - 1)) or (s[start] == s[end - 1] and isPalindrome(start + 1, end - 2))
        return True
            
                
            
                