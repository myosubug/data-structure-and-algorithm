class TrieNode():
    def __init__(self):
        self.lookup = {}
        self.end = False
    
    def addWord(self, word):
        current = self
        for c in word:
            if c not in current.lookup:
                current.lookup[c] = TrieNode()
            current = current.lookup[c]
        current.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        row, col, ret, visit = len(board), len(board[0]), set(), set()

        for w in words:
            root.addWord(w)

        for i in range(row):
            for j in range(col):
                self.dfs(i, j, row, col, board, root, ret, visit, "")
    
        return list(ret)

    def dfs(self, i, j, row, col, board, node, ret, visit, word):
        if not(0 <= i < row) or not (0 <= j < col) or (i, j) in visit or board[i][j] not in node.lookup:
            return

        c = board[i][j]

        visit.add((i,j))
        node = node.lookup[c]
        word += c
        if node.end:
            ret.add(word)

        self.dfs(i+1, j, row, col, board, node, ret, visit, word)
        self.dfs(i-1, j, row, col, board, node, ret, visit, word)
        self.dfs(i, j+1, row, col, board, node, ret, visit, word)
        self.dfs(i, j-1, row, col, board, node, ret, visit, word)

        visit.remove((i,j))
        
