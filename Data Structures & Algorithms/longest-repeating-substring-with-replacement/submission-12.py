class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        left = 0
        longest = 0
        most_frequent_count = 0

        for right, ch in enumerate(s):
            current_count = lookup.get(ch, 0) + 1
            lookup[ch] = current_count
            most_frequent_count = max(most_frequent_count, current_count)

            while right - left + 1 - k > most_frequent_count:
                lookup[s[left]] -= 1
                left += 1
                if lookup[s[left]] == 0:
                    del lookup[s[left]]

            longest = max(longest, right-left+1)

        return longest
