class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = []

        def helper(index, cur_sum):
            if cur_sum == target:
                ret.append(temp.copy())
                return
            
            if cur_sum > target or index >= len(nums):
                return

            helper(index+1, cur_sum)

            temp.append(nums[index])
            helper(index, cur_sum + nums[index])
            temp.pop()

        helper(0, 0)

        return ret