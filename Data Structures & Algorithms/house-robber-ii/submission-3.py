class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.search(nums[:-1]), self.search(nums[1:]))


    def search(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [0] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])

        return memo[-1]