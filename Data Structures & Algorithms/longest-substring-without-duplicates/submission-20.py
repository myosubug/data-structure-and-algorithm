class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        counter = {}
        l = 0

        for r, c in enumerate(s):
            while c in counter:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            
            counter[c] = 1
            longest = max(longest, r-l+1)
        
        return longest