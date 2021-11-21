class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sum = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            sum += abs(seats[i] - students[i])
        
        return sum