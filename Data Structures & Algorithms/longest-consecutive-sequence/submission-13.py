class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ret_counter = 0

        for n in nums:
            if n-1 not in num_set:
                i = n
                temp_counter = 0
                while i in num_set:
                    temp_counter += 1
                    i += 1
                ret_counter = max(ret_counter, temp_counter)

        return ret_counter