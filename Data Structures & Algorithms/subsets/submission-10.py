class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []


        def helper(carry, idx):
            if idx == len(nums):
                ret.append(carry.copy())
                return
            
            carry.append(nums[idx])
            helper(carry, idx+1)

            carry.pop()
            helper(carry, idx+1)

        helper([], 0)

        return ret