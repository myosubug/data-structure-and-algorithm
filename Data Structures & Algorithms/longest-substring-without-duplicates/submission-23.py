class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        longest = 0
        left = 0

        for right, c in enumerate(s):
            while c in lookup:
                del lookup[s[left]]
                left += 1
            lookup[c] = right
            longest = max(longest, right-left+1)

        return longest