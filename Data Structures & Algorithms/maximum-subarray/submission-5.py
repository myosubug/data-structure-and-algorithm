class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        temp = 0
        for i, n in enumerate(nums):
            temp += n
            maximum = max(maximum, temp)
            if temp < 0:
                temp = 0


        return maximum