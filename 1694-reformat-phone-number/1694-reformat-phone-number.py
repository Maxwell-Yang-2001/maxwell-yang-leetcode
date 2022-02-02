class Solution:
    def reformatNumber(self, number: str) -> str:
        for i in range(len(number))[::-1]:
            # not a number
            if number[i] == ' ' or number[i] == '-':
                number = number[:i] + number[i+1:]
        
        group_of_3 = (len(number) - 2) // 3
        
        result = ''
        for i in range(group_of_3):
            result += number[i*3:(i+1)*3] + '-'
        
        remain_len = len(number) - 3 * group_of_3
        
        if remain_len == 4:
            result += number[-4:-2] + '-' + number[-2:]
        else:
            result += number[-remain_len:]
        
        return result