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
        

        def helper(idx, node):
            current = node
            for i in range(idx, len(word)):
                if word[i] == ".":
                    for child in current.lookup.values():
                        if helper(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in current.lookup:
                        return False
                    else:
                        current = current.lookup[word[i]]
            return current.end

        return helper(0, self.root)    
                
