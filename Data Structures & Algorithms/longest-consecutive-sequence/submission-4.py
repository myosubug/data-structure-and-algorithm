class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in lookup:
                temp = n
                streak = 0
                while temp in lookup:
                    streak += 1
                    temp += 1
                longest = max(longest, streak)

        return longest
