class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        occurence = dict()
        largest = 0
        for pile in piles:
            largest = max(largest, pile)
            if pile in occurence:
                occurence[pile] += 1
            else:
                occurence[pile] = 1
        
        # binary search
        left = 1
        right = largest
        
        while right > (left + 1):
            middle = (left + right) // 2
            hours_needed = 0
            
            for banana in occurence:
                hours_needed += ((banana + middle - 1) // middle) * occurence[banana]
            
            if hours_needed <= h:
                right = middle
            else:
                left = middle
            
        hours_needed = 0
            
        for banana in occurence:
            hours_needed += ((banana + right - 1) // left) * occurence[banana]
            
        return left if hours_needed <= h else right
            
            
        
        