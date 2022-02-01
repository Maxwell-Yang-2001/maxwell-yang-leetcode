class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda n: n[0])
        
        # in_group: which group is i in
        in_group = dict()
        
        # groups: members in each group
        groups = [[i] for i in range(n)]
        for i in range(n):
            in_group[i] = i
        
        counter = n - 1
        for log in logs:
            group1_num, group2_num = in_group[log[1]], in_group[log[2]]
            if group1_num == group2_num:
                continue
                
            # counter reaches 0: we combine n - 1 times, so now there is only 1 group
            counter -= 1
            if counter == 0:
                return log[0]
            
            group_clear, group_add = groups[group1_num], groups[group2_num]
            
            # add everything in group_clear to group_add, no need to clear from old list
            for i in group_clear:
                group_add.append(i)
                in_group[i] = group2_num
            
        return -1