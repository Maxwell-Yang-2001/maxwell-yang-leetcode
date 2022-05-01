class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # start at 0, then shift afterwards
        result = [0] * (1 + len(s))
        stack = []
        result_index = 0
        for i, c in enumerate(s):
            stack.append(i + 1)
            if c == 'I':
                while stack:
                    result[result_index] = stack.pop()
                    result_index += 1
        stack.append(len(s) + 1)
        while stack:
            result[result_index] = stack.pop()
            result_index += 1
        return result