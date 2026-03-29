class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = -1
        idx = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > length:
                    length = r-l+1
                    idx = l
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > length:
                    length = r-l+1
                    idx = l
                l -= 1
                r += 1
        return s[idx:idx+length]