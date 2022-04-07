class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)
        freq = [0] * (max_weight + 1)
        
        def findNext(end: int) -> int:
            curr = end
            while curr >= 0 and freq[curr] == 0:
                curr -= 1
            return curr
        
        for s in stones:
            freq[s] += 1
        
        curr = max_weight
        while curr >= 0:
            freq[curr] %= 2
            if freq[curr] == 1:
                smaller = findNext(curr - 1)
                # only 1 stone left
                if smaller == -1:
                    return curr
                # smash inequally
                freq[smaller] -= 1
                freq[curr] -= 1
                freq[curr - smaller] += 1
                if freq[smaller] > 0:
                    curr = max(smaller, curr - smaller)
                elif smaller < curr - smaller:
                    curr -= smaller
                else:
                    curr = findNext(smaller - 1)
            else:
                larger = findNext(curr - 1)
                # no stone found
                if larger < 0:
                    return 0
                if freq[larger] > 1:
                    freq[larger] -= 2
                    curr = larger
                else:
                    smaller = findNext(larger - 1)
                    # only 1 stone left
                    if smaller < 0:
                        return larger
                    # smash inequally
                    freq[smaller] -= 1
                    freq[larger] -= 1
                    freq[larger - smaller] += 1
                    if freq[smaller] > 0:
                        curr = max(smaller, curr - smaller)
                    elif smaller < curr - smaller:
                        curr -= smaller
                    else:
                        curr = findNext(smaller - 1)
        return 0