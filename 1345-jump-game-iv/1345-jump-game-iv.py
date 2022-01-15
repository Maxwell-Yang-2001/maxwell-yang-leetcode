class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        if len(arr) <= 1:
            return 0
        
        visited = set()
        occurence_dict = dict()
        
        last = len(arr) - 1
        
        # set up occurences for same number
        for i, n in enumerate(arr):
            if n in occurence_dict:
                occurence_dict[n].append(i)
            else:
                occurence_dict[n] = [i]
        
        # use -1 to represent end of one level
        toDo = set([0])
        otherToDo = set([last])
        saveNext = set()
        jumps = 1
        
        # since BFS is always going to find the last element, we could ignore checking conditions
        while True:
            curr = toDo.pop()

            # consider left, right and occurence_dict
            visited.add(curr)
            if curr != 0:
                if (curr - 1) in otherToDo:
                    return jumps
                elif (curr - 1) not in visited:
                    saveNext.add(curr - 1)
                
            if curr != last:
                if (curr + 1) in otherToDo:
                    return jumps
                elif (curr + 1) not in visited:
                    saveNext.add(curr + 1)
                
            for i_other_occurence in occurence_dict[arr[curr]]:
                if i_other_occurence in otherToDo:
                    return jumps
                elif i_other_occurence not in visited:
                    saveNext.add(i_other_occurence)
            
            # end of a BFS level
            if len(toDo) == 0:
                jumps += 1
                saveNext, toDo = toDo, saveNext
                if len(toDo) > len(otherToDo):
                    toDo, otherToDo = otherToDo, toDo
        # not possible, but add it anyway
        return -1
                