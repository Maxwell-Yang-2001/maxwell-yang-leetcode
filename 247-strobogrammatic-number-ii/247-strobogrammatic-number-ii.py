class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # single digit: 0, 1, 8
        # double digits: 11, 69, 88, 96, 00
        # double digits on edge: 11, 69, 88, 96
        
        result = ['0', '1', '8'] if n % 2 == 1 else ['']
        
        double_digits = [['1', '1'], ['8', '8'], ['6', '9'], ['9', '6'], ['0', '0']]
        
        for i in range(n // 2 - 1):
            for j in range(len(result)):
                for k in double_digits[1:]:
                    result.append(k[0] + result[j] + k[1])
                result[j] = double_digits[0][0] + result[j] + double_digits[0][1]
        
        double_digits = [['1', '1'], ['8', '8'], ['6', '9'], ['9', '6']]
        
        if n >= 2:
            for j in range(len(result)):
                for k in double_digits[1:]:
                    result.append(k[0] + result[j] + k[1])
                result[j] = double_digits[0][0] + result[j] + double_digits[0][1]
        
        return result
                