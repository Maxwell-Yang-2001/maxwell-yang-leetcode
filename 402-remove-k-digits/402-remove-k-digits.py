class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        counter = 0
        stack = []
        
        for c in num:
            while counter < k and stack and c < stack[-1]:
                stack.pop()
                counter += 1
            stack.append(c)
        
        if counter < k:
            stack = stack[:-(k - counter)]
        
        return ''.join(stack).lstrip('0') or '0'
            