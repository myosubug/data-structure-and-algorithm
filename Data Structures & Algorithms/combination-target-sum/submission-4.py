class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, temp = [], []

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(temp.copy())
                return

            if cur_sum > target or i == len(nums):
                return

            ## not using
            backtrack(i+1, cur_sum)


            ## using
            temp.append(nums[i])
            backtrack(i, cur_sum+nums[i])

            temp.pop()

        backtrack(0,0)

        return res