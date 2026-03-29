class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
                return
            
            for c in range(n):
                if self.safe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."

        backtrack(0)
        return ret

    def safe(self, r, c, board):
        row = r-1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1

        row, col = r-1, c-1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r-1, c+1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True
        
