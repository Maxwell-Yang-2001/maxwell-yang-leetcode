class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can = capacity
        steps = 0
        for i, p in enumerate(plants):
            can -= p
            if can < 0:
                can = capacity - p
                steps += 2 * i + 1
            else:
                steps += 1
        return steps