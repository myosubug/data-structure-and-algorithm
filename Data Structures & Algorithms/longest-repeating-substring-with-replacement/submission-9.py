class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_char = 0
        longest = 0
        l = 0
        counter = {}

        for r, c in enumerate(s):
            current_c = counter.get(c, 0) + 1
            counter[c] = current_c
            max_char = max(max_char, current_c)

            while r-l+1-k > max_char:
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)

        return longest
