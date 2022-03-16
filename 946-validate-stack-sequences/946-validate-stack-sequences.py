class Solution:
    def validateStackSequences(self, pushed, popped):
        i = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return i == len(popped)