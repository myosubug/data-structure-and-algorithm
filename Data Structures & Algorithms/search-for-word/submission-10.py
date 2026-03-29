class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])


        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    check = self.helper(i, j, row, col, board, 0, word)
                    if check:
                        return True
        
        return False

    def helper(self, i, j, row, col, board, index, word):
        if index == len(word):
            return True

        if not (0 <= i < row) or not (0 <= j < col) or board[i][j] != word[index]:
            return False
        
        
        board[i][j] = "$"
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            if self.helper(i+dx, j+dy, row, col, board, index+1, word):
                return True
        
        board[i][j] = word[index]

        
        