class TrieNode:
    def __init__(self):
        self.lookup = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.lookup:
                current.lookup[c] = TrieNode()
            current = current.lookup[c]
        current.end = True


    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.lookup:
                return False
            current = current.lookup[c]
        
        return True if current.end else False 
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.lookup:
                return False
            current = current.lookup[c]
        
        return True 

        
        
        