class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = countChars(s)
        tdict = countChars(t)

        for k in sdict:
            if k not in tdict or sdict[k] != tdict[k]:
                return False
        
        return True
        
def countChars(s):
    ret = {}
    for ch in s:
        if ch in ret:
            ret[ch] += 1
        else:
            ret[ch] = 1
        
    return ret