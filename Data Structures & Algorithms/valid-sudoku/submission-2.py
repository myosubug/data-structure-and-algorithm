class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRow(board) and self.checkColumn(board) and self.checkBox(board)

    def checkRow(self, board):
        for row in board:
            if not self.checkDigits(row):
                return False
        return True
    def checkColumn(self, board):
        for j in range(len(board[0])):
            temp_col = []
            for i in range(len(board)):
                temp_col.append(board[i][j])
            if not self.checkDigits(temp_col):
                return False
        return True
    
    def checkBox(self, board):
        center = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]

        for x,y in center:
            temp_row = [board[x][y]]
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]:
                temp_row.append((board[x+dx][y+dy]))
            if not self.checkDigits(temp_row):
                return False
        return True
    
    def checkDigits(self, arr):
        lookup = {i: False for i in range(1, 10)}
        for n in arr:
            h = -1
            if n != ".":
                h = int(n)
            else:
                continue
            if h in lookup:
                if lookup[h]:
                    return False
                else:
                    lookup[h] = True
            else:
                return False
        
        return True