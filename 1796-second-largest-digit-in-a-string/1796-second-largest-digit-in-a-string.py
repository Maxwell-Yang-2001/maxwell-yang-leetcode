class Solution:
    def secondHighest(self, s: str) -> int:
        largest, secondLargest = -1, -1
        for c in s:
            if c.isdecimal():
                if int(c) > largest:
                    secondLargest = largest
                    largest = int(c)
                else:
                    if int(c) < largest and int(c) > secondLargest:
                        secondLargest = int(c)
        return secondLargest