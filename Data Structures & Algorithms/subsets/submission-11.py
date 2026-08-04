class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ret = []

        def helper(idx):
            if idx == len(nums):
                ret.append(path.copy())
                return

            path.append(nums[idx])
            helper(idx+1)
            path.pop()

            helper(idx+1)

        helper(0)

        return ret