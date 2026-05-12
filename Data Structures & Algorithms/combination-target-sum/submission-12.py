class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        ret = []

        def helper(idx, cur_sum):
            if cur_sum == target:
                ret.append(path.copy())
                return

            if idx == len(nums) or cur_sum > target:
                return
            
            helper(idx+1, cur_sum)

            path.append(nums[idx])
            helper(idx, cur_sum+nums[idx])
            path.pop()

        helper(0, 0)

        return ret