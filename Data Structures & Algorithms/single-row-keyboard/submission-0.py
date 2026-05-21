class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        lookup = {}
        for i, n in enumerate(keyboard):
            lookup[n] = i

        ret = lookup[word[0]]
        for j in range(1, len(word)):
            diff = abs(lookup[word[j]] - lookup[word[j-1]])
            ret += diff

        return ret
            