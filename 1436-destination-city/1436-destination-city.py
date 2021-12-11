class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # cityMap contains the dict of all cities that are either sources or dests but not both
        # source is True, dest is False
        cityMap = dict()
        for p in paths:
            if p[0] in cityMap:
                cityMap.pop(p[0])
            else:
                cityMap[p[0]] = True
            
            if p[1] in cityMap:
                cityMap.pop(p[1])
            else:
                cityMap[p[1]] = False
        
        for c in cityMap:
            if cityMap[c] == False:
                return c
        
        return ''