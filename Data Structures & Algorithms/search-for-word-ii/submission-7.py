class TrieNode:
    def __init__(self):
        self.lookup = {}
        self.end = False
    
    def add(self, word):
        current = self
        for c in word:
            if c not in current.lookup:
                current.lookup[c] = TrieNode()
            current = current.lookup[c]
        current.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ret = set()
        t = TrieNode()
        col, row = len(board[0]), len(board)
        visit = set()

        for w in words:
            t.add(w)

        for i in range(row):
            for j in range(col):
                self.helper(i, j, row, col, board, t, ret, visit, "")
        
        return list(ret)
    
    def helper(self, i, j, row, col, board, trie, ret, visit, word):
        if not (0 <= i < row) or not (0 <= j < col) or (i,j) in visit or board[i][j] not in trie.lookup:
            return

        c = board[i][j]
        visit.add((i,j))
        node = trie.lookup[c]
        word += c
        if node.end:
            ret.add(word)

        self.helper(i+1, j, row, col, board, node, ret, visit, word) 
        self.helper(i-1, j, row, col, board, node, ret, visit, word) 
        self.helper(i, j+1, row, col, board, node, ret, visit, word) 
        self.helper(i, j-1, row, col, board, node, ret, visit, word) 

        visit.remove((i,j))

        