class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        
        for c in s[1:]:
            if c == 'a':
                deletions += 1

        minDeletions = deletions
        if s[0] == 'b':
            deletions += 1
        
        for c in s[1:]:
            if c == 'a':
                deletions -= 1
            minDeletions = min(deletions, minDeletions)
            if c == 'b':
                deletions += 1
        
        return minDeletions
                
            
        