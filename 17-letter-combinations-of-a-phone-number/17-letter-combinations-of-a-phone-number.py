class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                 ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        
        result_size = 1
        for d in digits:
            index = ord(d) - ord('0')
            result_size *= len(mapping[index])
        
        result = [''] * result_size
        
        choices = mapping[ord(digits[0]) - ord('0')]
        for i, c in enumerate(choices):
            result[i] += c
        
        curr_size = len(choices)
            
        for d in digits[1:]:
            choices = mapping[ord(d) - ord('0')]
            for i in range(curr_size):
                result[i] += choices[0]
                for j, c in enumerate(choices[1:]):
                    curr_index = curr_size * (j + 1) + i
                    result[curr_index] = result[i][:-1] + c
            curr_size *= len(choices)
                    
        
        return result
        
            
            
            