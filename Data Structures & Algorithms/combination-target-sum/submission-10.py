class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        path = []

        def helper(cur, i):
            if cur == target:
                ret.append(path.copy())
                return

            if cur > target or i == len(nums):
                return

            helper(cur, i+1)

            path.append(nums[i])
            helper(cur+nums[i], i)
            path.pop()
            

        
        helper(0, 0)

        return ret