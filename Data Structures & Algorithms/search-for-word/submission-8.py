class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self.backtrack(i, j, row, col, 0, word, board):
                        return True
        

        return False

    def backtrack(self, i, j, row, col, index, word, board):
        if index == len(word):
            return True

        if not (0 <= i < row) or not (0 <= j < col) or board[i][j] != word[index]:
            return False
        
        
        board[i][j] = "$"
        if self.backtrack(i+0, j+1, row, col, index+1, word, board) or \
        self.backtrack(i+1, j+0, row, col, index+1, word, board) or \
        self.backtrack(i+0, j-1, row, col, index+1, word, board) or \
        self.backtrack(i-1, j+0, row, col, index+1, word, board):
            return True

        board[i][j] = word[index]
            
        