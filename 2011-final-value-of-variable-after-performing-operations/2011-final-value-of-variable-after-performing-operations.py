class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for o in operations:
            if o[1] == "+":
                result += 1
            else:
                result -= 1
        return result