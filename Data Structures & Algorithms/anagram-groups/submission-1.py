class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use map as a primary data structure
        # key : string
        # values: list of strings

        
        # iterate list of strings
            # sort each string
                # if sorted string exists, put original in the values
                # if sorted string doesn't exist, put it as a new key
        lookup = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in lookup:
                lookup[sorted_s].append(s)
            else:
                lookup[sorted_s] = [s]

        ret = []
        for k in lookup:
            ret.append(lookup[k])


        return ret