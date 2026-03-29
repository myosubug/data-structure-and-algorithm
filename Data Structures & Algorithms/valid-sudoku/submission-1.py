class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = 9, 9
        return self.isRowValid(board, row) and self.isColValid(board, row) and self.isSquareValid(board)

    def isRowValid(self, board, row):
        for row in board:
            lookup = {}
            for n in row:
                if n in lookup and n != ".":
                    return False
                lookup[n] = True
        return True

    def isColValid(self, board, row):
        for c in range(row):
            lookup = {}
            for i in range(row):
                num = board[i][c]
                if num in lookup and num != ".":
                    return False
                lookup[num] = True
        return True
    
    def isSquareValid(self, board):
        

        for ddx, ddy in [(0,0),(0,3),(0,6),(3,0),(6,0),(3,3),(3,6),(6,3),(6,6)]:
            x,y = 1,1
            x += ddx
            y += ddy
            lookup = {}
            for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
                num = board[x+dx][y+dy]
                if num in lookup and num != ".":
                    return False
                lookup[num] = True
        
        return True




