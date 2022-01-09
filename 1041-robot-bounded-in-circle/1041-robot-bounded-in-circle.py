class Solution:
    # direction: 0 - north, 1 - west, 2 - south, 3 - east
    def isRobotBounded(self, instructions: str) -> bool:
        # after 4 rounds, guarantee to be in same direction
        direction, x, y = 0, 0, 0
        for round in range(4):
            for i in instructions:
                if i == 'G':
                    if direction == 0:
                        y += 1
                    elif direction == 1:
                        x -= 1
                    elif direction == 2:
                        y -= 1
                    else:
                        x += 1
                elif i == 'L':
                    direction = (direction + 1) % 4
                else:
                    direction = (direction + 3) % 4
            if direction == 0:
                return x == 0 and y == 0
        return False
        