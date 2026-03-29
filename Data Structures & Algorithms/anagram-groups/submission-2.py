class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        lookup = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in lookup:
                lookup[sorted_s].append(s)
            else:
                lookup[sorted_s] = [s]

        for v in lookup.values():
            ret.append(v)

        return ret