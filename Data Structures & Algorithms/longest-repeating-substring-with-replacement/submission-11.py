class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        longest = 0
        left = 0
        most_frequent_counter = 0

        for right in range(len(s)):
            ch = s[right]
            current_count = lookup.get(ch, 0) + 1
            lookup[ch] = current_count
            most_frequent_counter = max(most_frequent_counter, current_count)

            while (right - left + 1) - k > most_frequent_counter:
                lookup[s[left]] -= 1
                left += 1
                if lookup[s[left]] == 0:
                    del lookup[s[left]]
            
            longest = max(longest, right - left + 1)

        return longest