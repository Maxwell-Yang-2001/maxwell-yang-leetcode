class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            if c == ')':
                val = stack.pop()
                stack[-1] += val * 2 if val > 0 else 1
        
        return stack[0]