class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        deletions = 0
        deletionsBase = 0

        minDeletions = 0
        if s[0] == 'b':
            deletions += 1
        
        for c in s[1:]:
            if c == 'a':
                deletions -= 1
                deletionsBase += 1
            minDeletions = min(deletions, minDeletions)
            if c == 'b':
                deletions += 1
        
        return minDeletions + deletionsBase
                
            
        