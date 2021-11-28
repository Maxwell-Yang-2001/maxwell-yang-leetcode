class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        totalTime = 0
        currentIndex = 0
        while True:
            totalTime += 1
            tickets[currentIndex] -= 1
            if tickets[currentIndex] == 0:
                if currentIndex == k:
                    return totalTime
                tickets.pop(currentIndex)
                if currentIndex < k:
                    k -= 1
            else:
                currentIndex += 1
            currentIndex = currentIndex % len(tickets)