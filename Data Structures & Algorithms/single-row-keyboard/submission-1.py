class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        lookup = {}
        for i, c in enumerate(keyboard):
            lookup[c] = i

        ret = 0 + lookup[word[0]]
        for j in range(1, len(word)):
            ret += abs(lookup[word[j]]-lookup[word[j-1]])
        
        return ret