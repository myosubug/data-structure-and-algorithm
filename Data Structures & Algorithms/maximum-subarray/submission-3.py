class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = -1
        i = 0
        temp_val = 0
        while i < len(nums):
            if temp_val + nums[i] < 0:
                i += 1
                temp_val = 0
            else:
                temp_val += nums[i]
                max_val = max(max_val, temp_val)
                i += 1

        return max_val
        