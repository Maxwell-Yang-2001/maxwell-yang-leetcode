class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        lookup = [-1] * 26 # map from word to pattern
        lookup_set = set()
        ord_a = ord('a')
        ord_pattern = [0] * len(pattern)
        for i in range(len(pattern)):
            ord_pattern[i] = ord(pattern[i]) - ord_a
        
        result = []
        for w in words:
            success = True
            for i in range(len(w)):
                ord_l = ord(w[i]) - ord_a
                if lookup[ord_l] == -1:
                    lookup[ord_l] = ord_pattern[i]
                    if ord_pattern[i] in lookup_set:
                        success = False
                        break
                    lookup_set.add(ord_pattern[i])
                elif lookup[ord_l] != ord_pattern[i]:
                    success = False
                    break

            if success:
                result.append(w)
            
            # cleanup
            for i in range(26):
                lookup[i] = -1
            lookup_set.clear()
        
        return result
                
                
                    