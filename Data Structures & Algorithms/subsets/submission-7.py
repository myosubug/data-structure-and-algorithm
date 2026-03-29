class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        temp = []

        def backtrack(index):
            if index >= len(nums):
                ret.append(temp.copy())
                return

            backtrack(index+1)
            
            temp.append(nums[index])
            backtrack(index+1)
            temp.pop()

        backtrack(0)

        return ret