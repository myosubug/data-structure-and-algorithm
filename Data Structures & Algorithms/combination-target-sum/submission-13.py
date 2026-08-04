class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        ret = []
        def helper(temp_sum, idx, target):
            if temp_sum > target or idx >= len(nums):
                return
            
            if temp_sum == target:
                ret.append(path.copy())
                return
            
            path.append(nums[idx])
            helper(temp_sum + nums[idx], idx, target)
            path.pop()

            helper(temp_sum, idx+1, target)

        helper(0, 0, target)

        return ret