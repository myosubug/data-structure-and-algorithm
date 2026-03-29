class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                res = max(cur, res)

        return res