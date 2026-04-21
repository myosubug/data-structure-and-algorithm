class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if i == 0:
                    self.helper(i, j, row, col, board)
                elif i == row-1:
                    self.helper(i, j, row, col, board)
                elif j == 0:
                    self.helper(i, j, row, col, board)
                elif j == col-1:
                    self.helper(i, j, row, col, board)

        for a in range(row):
            for b in range(col):
                if board[a][b] == "O":
                    board[a][b] = "X"
                elif board[a][b] == "N":
                    board[a][b] = "O"

    
    def helper(self, x, y, row, col, board):
        if not (0 <= x < row and 0 <= y < col) or board[x][y] != "O":
            return
        
        board[x][y] = "N"

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            self.helper(x+dx, y+dy, row, col, board)