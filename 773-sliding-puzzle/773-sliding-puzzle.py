class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        
        prev = set()
        curr = set()
        
        zeroPos = -1
        for i in range(6):
            if board[i // 3][i % 3] == 0:
                zeroPos = i + 1
                break
        
        initState = (zeroPos, board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2])

        prev.add(initState)
        level = 0
        
        # due to the characteristic of the maze (could go backwards), equal size of sets means we run out of paths to try
        while (len(prev) != len(curr)):
            curr.clear()
            
            for state in prev:
                if (state[1], state[2], state[3], state[4], state[5], state[6]) == target:
                    return level
                
                if state[0] == 1:
                    curr.add((2, state[2], state[1], state[3], state[4], state[5], state[6]))
                    curr.add((4, state[4], state[2], state[3], state[1], state[5], state[6]))
                elif state[0] == 2:
                    curr.add((1, state[2], state[1], state[3], state[4], state[5], state[6]))
                    curr.add((3, state[1], state[3], state[2], state[4], state[5], state[6]))
                    curr.add((5, state[1], state[5], state[3], state[4], state[2], state[6]))
                elif state[0] == 3:
                    curr.add((2, state[1], state[3], state[2], state[4], state[5], state[6]))
                    curr.add((6, state[1], state[2], state[6], state[4], state[5], state[3]))
                elif state[0] == 4:
                    curr.add((5, state[1], state[2], state[3], state[5], state[4], state[6]))
                    curr.add((1, state[4], state[2], state[3], state[1], state[5], state[6]))
                elif state[0] == 5:
                    curr.add((4, state[1], state[2], state[3], state[5], state[4], state[6]))
                    curr.add((6, state[1], state[2], state[3], state[4], state[6], state[5]))
                    curr.add((2, state[1], state[5], state[3], state[4], state[2], state[6]))
                else:
                    curr.add((5, state[1], state[2], state[3], state[4], state[6], state[5]))
                    curr.add((3, state[1], state[2], state[6], state[4], state[5], state[3]))
                            # set up prev and curr for next iteration
            
            tmp = prev
            prev = curr
            curr = tmp
            level += 1
        
        return -1