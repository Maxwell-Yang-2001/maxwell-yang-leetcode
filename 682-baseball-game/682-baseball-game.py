class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = deque([])
        score_sum = 0
        for o in ops:
            if o == '+':
                curr = records[-2] + records[-1]
                score_sum += curr
                records.append(curr)
            elif o == 'C':
                score_sum -= records.pop()
            elif o == 'D':
                curr = 2 * records[-1]
                score_sum += curr
                records.append(curr)
            else:
                curr = int(o)
                score_sum += curr
                records.append(curr)
        return score_sum
            