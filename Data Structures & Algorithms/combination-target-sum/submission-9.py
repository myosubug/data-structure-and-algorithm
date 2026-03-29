class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = []

        def helper(i, cur_sum):
            if cur_sum == target:
                ret.append(temp.copy())
                return

            if cur_sum > target or i == len(nums):
                return

            
            helper(i+1, cur_sum)

            temp.append(nums[i])
            helper(i, cur_sum + nums[i])
            temp.pop()

        helper(0, 0)

        return ret