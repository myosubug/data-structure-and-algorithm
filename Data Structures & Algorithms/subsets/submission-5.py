class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(temp.copy())
                return

            # not using
            backtrack(i+1)

            # use
            temp.append(nums[i])
            backtrack(i+1)
            
            temp.pop()

        backtrack(0)


        return res