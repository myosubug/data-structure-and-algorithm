class TrieNode:
    def __init__(self):
        self.lookup = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.lookup:
                current.lookup[c] = TrieNode()
            current = current.lookup[c]
        current.end = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            current = root        
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in current.lookup.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in current.lookup:
                        return False
                    current = current.lookup[c]
            return current.end

        return dfs(0, self.root)
            

        
