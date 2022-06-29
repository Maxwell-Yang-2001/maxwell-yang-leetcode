class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda n: -n[0]*2000+n[1])
        for i in range(len(people)):
            # alreay in place
            if people[i][1] == i:
                continue
            
            p = people.pop(i)
            people.insert(p[1], p)
        
        return people