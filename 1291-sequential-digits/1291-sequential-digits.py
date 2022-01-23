class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        log_low, log_high = int(log(low, 10)), int(log(high, 10))
        result = []
        
        for power in range(log_low, log_high + 1):
            for i in range(1, 10 - power):
                num = 0
                for curr_digit in range(i, i + power + 1):
                    num = 10 * num + curr_digit
                if num >= low and num <= high:
                    result.append(num)
        
        return result
            
        
        