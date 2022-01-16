class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # palindrome[i][j] == True means there is iji subsequence
        palindrome = [[False for i in range(26)] for j in range(26)]
        
        # first and last occurences for each letter
        letter_ranges = [[-1, -1] for i in range(26)]
        
        ord_a = ord('a')
        # first collect the start end
        for i, c in enumerate(s):
            val = ord(c) - ord_a
            if letter_ranges[val][0] == -1:
                letter_ranges[val][0] = i
            letter_ranges[val][1] = i
        
        result = 0
        # then go through again to check if in bound
        for i, c in enumerate(s):
            val = ord(c) - ord_a
            for j, ran in enumerate(letter_ranges):
                if not palindrome[j][val] and ran[0] < i and i < ran[1]:
                    palindrome[j][val] = True
                    result += 1
        
        return result
        