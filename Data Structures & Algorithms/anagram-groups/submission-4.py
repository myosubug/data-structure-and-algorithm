class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in lookup:
                lookup[sorted_s].append(s)
            else:
                lookup[sorted_s] = [s]
        
        return list(lookup.values())