class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stackGen(s: str) -> list:
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        stack_s, stack_t = stackGen(s), stackGen(t)
        return stack_s == stack_t
                        
                