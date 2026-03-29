class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        count = {}
        most_frequent = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            most_frequent = max(most_frequent, count[s[right]])

            while (right - left + 1) - most_frequent > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length
