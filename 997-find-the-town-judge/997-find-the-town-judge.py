class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        people = dict()
        for t in trust:
            if t[0] in people:
                people[t[0]][0] += 1
            else:
                people[t[0]] = [1, 0]
            if t[1] in people:
                people[t[1]][1] += 1
            else:
                people[t[1]] = [0, 1]
            
        target = [0, len(people) - 1]
        for p in people:
            if people[p] == target:
                return p
        return -1