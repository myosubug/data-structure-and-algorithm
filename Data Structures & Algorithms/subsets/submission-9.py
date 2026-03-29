class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []

        def helper(i):
            if i == len(nums):
                ret.append(path.copy())
                return
            
            path.append(nums[i])
            helper(i+1)
            
            path.pop()
            helper(i+1)

        helper(0)

        return ret