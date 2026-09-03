class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in seen:
                counter = 1
                while n + counter in seen:
                    counter += 1
                longest = max(longest, counter)

        return longest