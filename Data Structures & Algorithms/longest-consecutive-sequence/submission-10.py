class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        lookup = set(nums)

        for n in nums:
            if n-1 not in lookup:
                temp_len = 1
                i = 1
                while n + i in lookup:
                    temp_len += 1
                    i += 1
                longest = max(longest, temp_len)

        
        return longest