class Solution:
    def isValid(self, s: str) -> bool:
        def translate(c: str) -> int:
            if c == '(':
                return 1
            elif c == '[':
                return 2
            elif c == '{':
                return 3
            elif c == ')':
                return -1
            elif c == ']':
                return -2
            elif c == '}':
                return -3
        stack = []
        for c in s:
            val = translate(c)
            if val > 0:
                stack.append(val)
            elif stack:
                compliment = stack.pop()
                if compliment + val != 0:
                    return False
            else:
                # nothing to pop
                return False
        return not stack
            