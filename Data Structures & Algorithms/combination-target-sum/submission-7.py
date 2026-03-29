class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret, temp = [], []

        def dfs(i, cur_sum):
            if cur_sum == target:
                ret.append(temp.copy())
                return
            
            if i == len(nums) or cur_sum > target:
                return

            dfs(i+1, cur_sum)

            temp.append(nums[i])
            dfs(i, cur_sum + nums[i])
            temp.pop()


        dfs(0, 0)

        return ret