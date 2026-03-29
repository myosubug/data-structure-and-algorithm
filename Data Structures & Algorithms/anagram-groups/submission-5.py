class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        lookup = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in lookup:
                lookup[sorted_word].append(word)
            else:
                lookup[sorted_word] = [word]

        for v in lookup.values():
            ret.append(v)

        return ret