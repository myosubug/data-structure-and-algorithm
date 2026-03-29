class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self.search(i, j, row, col, 0, board, word):
                        return True

        
        return False


    def search(self, i, j, row, col, index, board, word):
        if index == len(word):
            return True
        
        if i < 0 or i >= row or j < 0 or j >= col or word[index] != board[i][j]:
            return False
        
        board[i][j] = "$"
        if self.search(i+1, j, row, col, index+1, board, word) or \
        self.search(i, j+1, row, col, index+1, board, word) or \
        self.search(i-1, j, row, col, index+1, board, word) or \
        self.search(i, j-1, row, col, index+1, board, word):
            return True
        
        board[i][j] = word[index]