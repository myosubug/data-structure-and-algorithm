class Solution:
    def scoreOfString(self, s: str) -> int:
        i, j = 0, 1
        ret = 0

        while j < len(s):
            ch1 = s[i]
            ch2 = s[j]
            ret += abs(ord(ch1)-ord(ch2))
            i += 1
            j += 1

        return ret