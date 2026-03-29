class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in nums:
            if (n-1) not in num_set:
                counter = 0
                i = 0
                while n+i in num_set:
                    counter += 1
                    i += 1
                longest = max(longest, counter)

        return longest