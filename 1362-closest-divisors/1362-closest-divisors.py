class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        best1, best2 = None, None
        diff1, diff2 = -1, -1
        for i in range(floor(sqrt(num + 2)), 0, -1):
            if (num + 1) % i == 0 and diff1 < 0:
                other = (num + 1) // i
                best1 = [i, other]
                diff1 = other - i
                if diff2 >= 0:
                    break
            if (num + 2) % i == 0 and diff2 < 0:
                other = (num + 2) // i
                best2 = [i, other]
                diff2 = other - i
                if diff1 >= 0:
                    break
        
        return best1 if diff1 < diff2 else best2