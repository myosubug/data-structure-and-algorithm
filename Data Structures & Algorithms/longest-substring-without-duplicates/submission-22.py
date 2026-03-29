class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        left = 0
        longest = 0

        for right, c in enumerate(list(s)):
            if c in lookup:
                while c in lookup:
                    del lookup[s[left]]
                    left += 1
            
            lookup[c] = right
            longest = max(longest, right-left+1)

        return longest