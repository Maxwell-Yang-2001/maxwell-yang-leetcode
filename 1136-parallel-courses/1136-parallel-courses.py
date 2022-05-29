class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        pre_dict, post_dict = defaultdict(lambda: set()), defaultdict(lambda: set())
        for a, b in relations:
            pre_dict[b - 1].add(a - 1)
            post_dict[a - 1].add(b - 1)
        
        iterations = 0
        courses = n
        
        totake = []
        for i in range(n):
            if i not in pre_dict:
                totake.append(i)
        
        while totake:
            next_totake = []
            for c in totake:
                # remove prereq from courses that needs c as a prereq
                for post_c in post_dict[c]:
                    pre_dict[post_c].remove(c)
                    if not pre_dict[post_c]:
                        del pre_dict[post_c]
                        next_totake.append(post_c)
                
                del post_dict[c]
            
            totake = next_totake
            next_totake = []
            iterations += 1
        
        return -1 if pre_dict else iterations
        