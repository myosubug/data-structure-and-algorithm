class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        seen = set()

        for right, c in enumerate(s):
            if c in seen:
                while c in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(c)
            longest = max(longest, right-left+1)
        
        return longest
        
        # seen = set()
        # longest = 0
        # l, r = 0, 0

        # while r < len(s):
        #     temp_c = s[r]
        #     if temp_c not in seen:
        #         longest = max(longest, r-l+1)
        #         seen.add(s[r])
        #         r += 1
        #     else:
        #         while s[l] in seen:
        #             seen.remove(s[l])
        #             l += 1

        # return longest