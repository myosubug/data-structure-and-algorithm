class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        longest = 0
        left = 0
        max_char = 0

        for right, c in enumerate(s):
            seen[c] = 1 + seen.get(c, 0)
            max_char = max(max_char, seen[c])

            while right-left + 1 - max_char > k:
                seen[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)

        return longest