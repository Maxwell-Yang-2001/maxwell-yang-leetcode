class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        counter = 0
        startIndex = 0
        for i, c in enumerate(s):
            if c == '(':
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                result += s[startIndex + 1 : i]
                startIndex = i + 1
        
        return result