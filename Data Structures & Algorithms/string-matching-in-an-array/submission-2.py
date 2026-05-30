class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = set()

        for i, w in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j and w in w2:
                    ret.add(w)

        return list(ret)