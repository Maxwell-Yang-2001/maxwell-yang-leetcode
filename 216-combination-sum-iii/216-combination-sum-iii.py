class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def recur(target, combination, start):
            if len(combination) == k:
                if target == 0:
                    result.append(list(combination))
                return
        
            for i in range(start, 10):
                combination.append(i)
                recur(target - i, combination, i + 1)
                combination.pop()
        
        recur(n, [], 1)
        return result