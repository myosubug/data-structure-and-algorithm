class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        left = 0
        longest = 0

        for right, c in enumerate(list(s)):
            current_count = count.get(c, 0) + 1
            count[c] = current_count

            max_count = max(max_count, current_count)

            while right-left+1-max_count > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)

        return longest