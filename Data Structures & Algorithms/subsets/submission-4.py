class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []


        def backtrack(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            backtrack(i+1)
            
            subsets.pop()
            backtrack(i+1)

        backtrack(0)

        return res
