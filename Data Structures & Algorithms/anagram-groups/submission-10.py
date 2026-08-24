class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        lookup = {}

        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in lookup:
                lookup[sorted_word] = []
            lookup[sorted_word].append(word)

        for values in lookup.values():
            ret.append(values)

        return ret