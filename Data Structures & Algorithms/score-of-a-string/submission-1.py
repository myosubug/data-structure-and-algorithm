class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 1
        ret = 0
        while j < len(s):
            ret += abs(ord(s[j])-ord(s[i]))
            i += 1
            j += 1

        return ret