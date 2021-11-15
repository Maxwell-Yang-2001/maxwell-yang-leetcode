class Solution:
    def average(self, salary: List[int]) -> float:
        lowest, highest = salary[0], salary[0]
        sum = 0
        
        for s in salary:
            lowest = min(lowest, s)
            highest = max(highest, s)
            sum += s
        
        return (sum - lowest - highest) / (len(salary) - 2)