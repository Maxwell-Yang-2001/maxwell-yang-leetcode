class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        ls, lp = len(s), len(p)
        if ls < lp:
            return result
        
        curr_dict, p_dict = dict(), dict()
        mismatches = 26
        
        # set up two dictionaries
        for i in range(ord('a'), ord('z') + 1):
            c = chr(i)
            curr_dict[c] = p_dict[c] = 0
            
        for c in p:
            p_dict[c] += 1
        
        for c in s[:lp]:
            curr_dict[c] += 1
        
        # calculate initial mismatches
        for c in p_dict:
            if p_dict[c] == curr_dict[c]:
                mismatches -= 1
        
        if mismatches == 0:
            result.append(0)
        
        for i in range(lp, ls):
            removed, added = s[i - lp], s[i]
            
            if removed != added:
                curr_dict[removed] -= 1
                curr_dict[added] += 1
                if curr_dict[removed] == p_dict[removed]:
                    mismatches -= 1
                elif curr_dict[removed] == p_dict[removed] - 1:
                    mismatches += 1
                if curr_dict[added] == p_dict[added]:
                    mismatches -= 1
                elif curr_dict[added] == p_dict[added] + 1:
                    mismatches += 1
            
            if mismatches == 0:
                result.append(i - lp + 1)
        
        return result
            
            
                