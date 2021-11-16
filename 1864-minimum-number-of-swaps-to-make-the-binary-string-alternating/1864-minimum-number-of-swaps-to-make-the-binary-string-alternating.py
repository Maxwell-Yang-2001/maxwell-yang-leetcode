class Solution:
    def minSwaps(self, s: str) -> int:
        zero = True
        wrongCounter = 0
        zeroCount = 0
        for c in s:
            if c == "1":
                if zero:
                    wrongCounter += 1
            else:
                zeroCount += 1
                if not zero:
                    wrongCounter += 1
            zero = not zero
        if len(s) % 2 == 0:
            if zeroCount != len(s) // 2:
                return -1
            else:
                return min(wrongCounter, len(s) - wrongCounter) // 2
        else:
            if zeroCount != len(s) // 2 and zeroCount != (len(s) // 2 + 1):
                return -1
            else:
                return wrongCounter // 2 if wrongCounter % 2 == 0 else (len(s) - wrongCounter) // 2