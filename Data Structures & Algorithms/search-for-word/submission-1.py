class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j, r, c):
                        return True
        
        return False


    def dfs(self, board, word, index, i, j, r, c):
        if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != word[index]:
            return False
        if index == len(word) - 1:
            return True
        
        board[i][j] = "$"

        if (self.dfs(board, word, index+1, i+1, j, r, c)
            or self.dfs(board, word, index+1, i-1, j, r, c)
            or self.dfs(board, word, index+1, i, j+1, r, c)
            or self.dfs(board, word, index+1, i, j-1, r, c)):
                return True

        board[i][j] = word[index]

        return False
        
        
      
            