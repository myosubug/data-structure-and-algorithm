class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRow(board) and self.checkCol(board) and self.checkBox(board)
    def stringToNums(self, l):
        ret = []
        for n in l:
            if n != ".":
                ret.append(int(n))
        return ret

    def checkRow(self, board):
        for i in range(len(board)):
            s = self.stringToNums(board[i])
            c = Counter(s)
            if len(s) != len(c):
                return False
        return True
    
    def checkCol(self, board):
        for j in range(len(board)):
            col = [row[j] for row in board]
            s = self.stringToNums(col)
            c = Counter(s)
            if len(s) != len(c):
                return False
        return True
    
    def checkBox(self, board):
        temp = []
        for x, y in [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]:
            temp_collection = []
            for dx, dy in [(1,0),(-1,0),(0,0),(1,1),(-1,1),(0,1),(1,-1),(-1,-1),(0,-1)]:
                temp_collection.append(board[x+dx][y+dy])
            s = self.stringToNums(temp_collection)
            c = Counter(s)
            if len(s) != len(c):
                return False
        return True
