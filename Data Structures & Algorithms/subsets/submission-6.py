class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        temp = []

        def helper(i):
            if i == len(nums):
                ret.append(temp.copy())
                return

            helper(i+1)

            temp.append(nums[i])
            helper(i+1)
            temp.pop()

        helper(0)

        return ret