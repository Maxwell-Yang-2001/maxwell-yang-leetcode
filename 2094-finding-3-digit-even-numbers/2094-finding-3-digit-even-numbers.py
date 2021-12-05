class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        occ = [0] * 10
        for digit in digits:
            occ[digit] += 1
        result = []
        for first in range(1, 10):
            if occ[first] == 0:
                continue
            occ[first] -= 1
            for second in range(0, 10):
                if occ[second] == 0:
                    continue
                occ[second] -= 1
                for third in range(0, 10, 2):
                    if occ[third] == 0:
                        continue
                    result.append(first * 100 + second * 10 + third)
                occ[second] += 1
            occ[first] += 1
        
        return result