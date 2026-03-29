class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.getHashMapFromString(s)
        t_map = self.getHashMapFromString(t) 

        if len(s_map) != len(t_map):
            return False

        for key in s_map.keys():
            if key not in t_map or s_map[key] != t_map[key]:
                return False
        return True

    def getHashMapFromString(self, s):
        ret = {}
        for c in s:
            if c in ret:
                ret[c] += 1
            else:
                ret[c] = 1
        return ret