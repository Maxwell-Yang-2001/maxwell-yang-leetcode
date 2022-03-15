class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index = len(s) - 1
        counter = 0
        
        while index >= 0:
            if s[index] == ')':
                counter += 1
            elif s[index] == '(':
                counter -= 1
            if counter == -1:
                counter = 0
                s = s[:index] + s[index + 1:]
            index -= 1

#         # do it in other direction
        counter, index = 0, 0
        
        while index < len(s):
            if s[index] == '(':
                counter += 1
            elif s[index] == ')':
                counter -= 1
            if counter == -1:
                counter = 0
                s = s[:index] + s[index + 1:]
                index -= 1
            index += 1
        
        return s