class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self.helper(board, row, col, i, j, 0, word):
                        return True

        return False

    def helper(self, board, row, col, i, j, idx, word):
        if not (0<= i< row) or not(0<= j <col) or word[idx] != board[i][j]:
            return False

        if idx == len(word)-1:
            return True


        temp = board[i][j]
        board[i][j] = '#'
        res = self.helper(board, row, col, i+0, j+1, idx+1, word) or self.helper(board, row, col, i+1, j+0, idx+1, word) or self.helper(board, row, col, i-1, j+0, idx+1, word) or self.helper(board, row, col, i+0, j-1, idx+1, word) 
        board[i][j] = temp
        return res