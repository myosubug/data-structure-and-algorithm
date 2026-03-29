class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, temp = [], []

        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(temp.copy())
                return

            if cur_sum > target or i == len(nums):
                return

            dfs(i+1, cur_sum)

            temp.append(nums[i])
            dfs(i, cur_sum + nums[i])
            temp.pop()

        dfs(0, 0)

        return res