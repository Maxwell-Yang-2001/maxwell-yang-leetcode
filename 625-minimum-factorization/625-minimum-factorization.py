class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1
        
        # num <= 2^31 - 1 = 2147483647. Should have at most 9 digits
        
        exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9 = 0, 0, 0, 0, 0, 0, 0, 0
        # prime divisors set-up
        while num % 2 == 0:
            num //= 2
            exp2 += 1
        while num % 3 == 0:
            num //= 3
            exp3 += 1
        while num % 5 == 0:
            num //= 5
            exp5 += 1
        while num % 7 == 0:
            num //= 7
            exp7 += 1
        
        if num != 1:
            return 0
        
        # maximize number of 8's, since it reduces digit count by 2 each time
        exp8 = exp2 // 3
        exp2 %= 3
        
        # maximize multiplication but still results in over 9 digits
        if exp8 + (exp2 + exp3 + 1) // 2 + exp5 + exp7 > 9:
            return 0
        
        reservedExp = 0
        # if there is an odd sum of 2's and 3's, reserve the minimum one here
        if (exp2 + exp3) % 2 == 1:
            if exp2 == 0:
                reservedExp = 3
                exp3 -= 1
            else:
                reservedExp = 2
                exp2 -= 1
        
        exp4 += exp2 // 2
        exp2 %= 2
        exp9 += exp3 // 2
        exp3 %= 2
        if exp2 == 1:
            exp2 = 0
            exp3 = 0
            exp6 += 1
        
        if reservedExp == 2:
            exp2 += 1
        elif reservedExp == 3:
            exp3 += 1
        
        result = 0
        expList = [exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9]
        print(expList)
        for i, exp in enumerate(expList):
            currentDigit = i + 2
            for j in range(exp):
                result = result * 10 + currentDigit
        
        return result
            