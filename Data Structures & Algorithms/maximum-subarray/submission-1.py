class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # res = nums[0]

        # for i in range(len(nums)):
        #     cur = 0
        #     for j in range(i, len(nums)):
        #         cur += nums[j]
        #         res = max(res, cur)

        # return res

        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        for r in dp:
            print(r)
        dp[n - 1][1] = dp[n - 1][0] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            # local
            dp[i][1] = max(nums[i], nums[i] + dp[i + 1][1])

            #global
            dp[i][0] = max(dp[i + 1][0], dp[i][1])
        
        return dp[0][0]