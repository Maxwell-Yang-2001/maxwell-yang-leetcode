class Solution:
    def generateTheString(self, n: int) -> str:
        l = ["a"] * ((n + 1) // 2 * 2 - 1)
        if n % 2 == 0:
            l.append("b")
        return "".join(l)