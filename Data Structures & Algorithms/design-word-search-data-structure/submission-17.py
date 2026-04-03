
class Node:
    def __init__(self):
        self.lookup = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.lookup:
                current.lookup[c] = Node()
            current = current.lookup[c]
        current.end = True

    def search(self, word: str) -> bool:
        def helper(node, idx):
            current = node
            for i in range(idx, len(word)):
                if word[i] == ".":
                    for child in current.lookup.values():
                        if helper(child, i+1):
                            return True
                    return False
                else:
                    if word[i] not in current.lookup:
                        return False
                    current = current.lookup[word[i]]
            return current.end


        return helper(self.root, 0)
