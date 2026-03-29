class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0

        for n in nums:
            temp_counter = 0
            if n-1 not in s:
                i = n+1
                temp_counter += 1
                while i in s:
                    temp_counter += 1
                    i += 1
            count = max(temp_counter, count)

        return count
