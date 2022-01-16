class Solution:
    def numWays(self, s: str) -> int:
        num_ones = 0
        for c in s:
            if c =='1':
                num_ones += 1
        
        if num_ones == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % (10 ** 9 + 7)
        elif num_ones % 3 != 0:
            return 0
        
        num_ones //= 3
        
        curr_num_ones = 0
        left_split_num_zeroes = 0
        right_split_num_zeroes = 0
        
        in_left_split = False
        in_right_split = False
        
        for i, c in enumerate(s):
            if c == '1':
                curr_num_ones += 1
                if curr_num_ones == num_ones:
                    in_left_split = True
                elif curr_num_ones == num_ones + 1:
                    in_left_split = False
                
                if curr_num_ones == 2 * num_ones:
                    in_right_split = True
                elif curr_num_ones == 2 * num_ones + 1:
                    in_right_split = False
            
            if in_left_split:
                left_split_num_zeroes += 1
            
            if in_right_split:
                right_split_num_zeroes += 1
        
        return (left_split_num_zeroes * right_split_num_zeroes) % (10 ** 9 + 7)