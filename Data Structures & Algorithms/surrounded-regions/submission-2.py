class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        row, col = len(board), len(board[0])

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

        for k in range(row):
            for l in range(col):
                if board[k][l] == "O":
                    board[k][l] = "X"
                elif board[k][l] == "B":
                    board[k][l] = "O"

    

    def helper(self, i, j, row, col, board):
        if not (0 <= i < row and 0 <= j < col) or board[i][j] != "O":
            return
        
        board[i][j] = "B"

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            self.helper(i+dx, j+dy, row, col, board)