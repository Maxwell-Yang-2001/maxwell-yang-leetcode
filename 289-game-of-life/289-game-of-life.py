class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        width, height = len(board[0]), len(board)
        
        # for in-place board, we do 2 rounds
        # round 1: value would be updated to be orig value + 2 * alive neighbors, to preserve oddity
        # round 2: compute the actual aliveness based on round 1
        for i in range(height):
            for j in range(width):
                neighbors = 0
                left, right, top, bottom = j > 0, j < width - 1, i > 0, i < height - 1
                if top:
                    # top left
                    if left and board[i - 1][j - 1] % 2 == 1:
                        neighbors += 1
                    # top
                    if board[i - 1][j] % 2 == 1:
                        neighbors += 1
                    # top right
                    if right and board[i - 1][j + 1] % 2 == 1:
                        neighbors += 1
                # left
                if left and board[i][j - 1] % 2 == 1:
                    neighbors += 1
                # right
                if right and board[i][j + 1] % 2 == 1:
                    neighbors += 1
                if bottom:
                    # bottom left
                    if left and board[i + 1][j - 1] % 2 == 1:
                        neighbors += 1
                    # bottom
                    if board[i + 1][j] % 2 == 1:
                        neighbors += 1
                    # bottom right
                    if right and board[i + 1][j + 1] % 2 == 1:
                        neighbors += 1
                
                board[i][j] += neighbors * 2
        
        for i in range(height):
            for j in range(width):
                # possible scenarios:
                # alive + 2 neighbors: 1 + 2 * 2 = 5
                # alive + 3 neighbors: 1 + 2 * 3 = 7
                # dead + 3 neighbors: 0 + 2 * 3 = 6
                board[i][j] = 1 if board[i][j] >= 5 and board[i][j] <= 7 else 0
        