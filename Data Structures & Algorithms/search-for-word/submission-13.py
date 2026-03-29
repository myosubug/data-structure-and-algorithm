class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        ret = False

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


   
        board[i][j] = '#'
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            if self.helper(board, row, col, i+dx, j+dy, idx+1, word):
                return True
        board[i][j] = word[idx]
