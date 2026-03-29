class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        count_window = {}
        max_char = 0

        for right, c in enumerate(s):
            count_window[c] = 1 + count_window.get(c, 0)
            max_char = max(max_char, count_window[c])

            while (right-left+1) - max_char > k:
                count_window[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)

        return longest
