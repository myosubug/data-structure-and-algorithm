class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self.helper(i, j, row, col, board, word, 0):
                        return True
        
        return False

    def helper(self, i, j, row, col, board, word, index):
        if index == len(word):
            return True

        if not (0 <= i < row) or not (0 <= j < col) or board[i][j] != word[index] or board[i][j] == "$":
            return False
        

        board[i][j] = "$"

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            if self.helper(i+dx, j+dy, row, col, board, word, index+1):
                return True

        board[i][j] = word[index]

