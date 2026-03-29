class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxf = 0
        counter = {}
        longest = 0


        for right, c in enumerate(s):
            counter[c] = 1 + counter.get(c, 0)
            maxf = max(maxf, counter[c])

            while (right-left+1) - maxf > k:
                counter[s[left]] -= 1
                left += 1
            
            longest = max(longest, right-left+1)

        return longest