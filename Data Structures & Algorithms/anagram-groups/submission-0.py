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
            sortedStr = ''.join(sorted(s))
            if sortedStr in lookup:
                lookup[sortedStr].append(s)
            else:
                lookup[sortedStr] = [s]
        
        ret = []
        for k in lookup:
            ret.append(lookup[k])

        return ret