class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True


        for i in range(n-2, -1, -1):
            # check farthest index from the current step
            # it's either less than len of nums or current index + the step it can take
            end = min(n, i + nums[i] + 1)

            # Checks if the current index i can reach the "end of the array"
            for j in range(i + 1, end):
                # if i can reach end, update i to be True as well
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]