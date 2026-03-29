class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        path = []

        def helper(carry, path, idx):
            if carry == target:
                ret.append(path.copy())
                return

            if idx == len(nums) or carry > target:
                return
            
            helper(carry, path, idx+1)

            path.append(nums[idx])
            helper(carry+nums[idx], path, idx)
            path.pop()

        helper(0, [], 0)


        return ret
