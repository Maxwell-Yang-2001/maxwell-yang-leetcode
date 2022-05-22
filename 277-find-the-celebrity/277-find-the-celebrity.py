# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        curr_group = [i for i in range(n)]
        
        candidate = 0
        # n - 1 calls to find a candidate
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        # 2n - 2 more calls tp find whether candidate is celebrity
        for i in range(n):
            if candidate != i and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        
        return candidate