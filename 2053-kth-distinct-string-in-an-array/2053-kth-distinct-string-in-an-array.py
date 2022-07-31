class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        visited = set()
        distinct = set()
        for s in arr:
            if s in distinct:
                distinct.remove(s)
            elif s not in visited:
                distinct.add(s)
            visited.add(s)
        
        for s in arr:
            if s in distinct:
                k -= 1
                if k == 0:
                    return s
        
        return ''
                
                
                