class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        seen = set()

        for right, c in enumerate(s):
            if c in seen:
                while c in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(c)
            longest = max(longest, right-left+1)

        return longest