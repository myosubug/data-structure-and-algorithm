class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            ch = s[right]
            while ch in lookup:
                del lookup[s[left]]
                left += 1
            lookup[ch] = 1
            
            longest = max(longest, right-left+1)
        return longest