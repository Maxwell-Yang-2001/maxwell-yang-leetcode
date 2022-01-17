class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        doubleLength = [('0','0'),('1','1'), ('6','9'),('8','8'),('9','6')]
        queue = collections.deque(['','0','1','8'])
        result = 0
        while queue:
            string = queue.popleft()
            if len(string) > len(high):
                break
            for left, right in doubleLength:
                queue.append(left + string + right)
            if len(string) > 0 and (int(low) <= int(string) <= int(high)):
                if len(string) > 1 and string[0] == '0':
                    continue
                result += 1
        return result