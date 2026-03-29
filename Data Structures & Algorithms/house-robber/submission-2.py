class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [1] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[1], nums[0])
 
        for i in range(2, len(nums)):
            memo[i] = max(nums[i]+memo[i-2], memo[i-1])


        return memo[-1]