class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            c = s[right]
            while c in seen:
                seen.remove(s[left])
                left += 1
            longest = max(longest, right-left+1)
            seen.add(c)
        
        return longest