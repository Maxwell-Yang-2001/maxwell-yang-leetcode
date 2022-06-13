class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        i = len(triangle)
        
        if i == 1:
            return triangle[0][0]
        mem = triangle[-1].copy()
        
        for i in range(i - 2, -1, -1):
            save = mem[1]
            mem[0] = min(mem[0], save) + triangle[i][0]
            for j in range(1, i + 1):
                new_save = mem[j + 1]
                mem[j] = min(save, new_save) + triangle[i][j]
                save = new_save
            
        return mem[0]