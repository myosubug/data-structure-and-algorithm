class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = {}
        max_char = 0
        left = 0

        for right, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            max_char = max(max_char, window[c])

            while (right-left+1) - max_char > k:
                window[s[left]] -= 1
                left += 1
            
            longest = max(longest, right-left+1)

        return longest