class TreeNode:
    def __init__(self):
        self.sub = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.sub:
                current.sub[c] = TreeNode()
            current = current.sub[c]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.sub:
                return False
            current = current.sub[c]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.sub:
                return False
            current = current.sub[c]
        
        return True
        
        