class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        lookup = set()
        left = 0

        for right in range(len(s)):
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1
            max_length = max(max_length, right-left+1)
            lookup.add(s[right])

        return max_length