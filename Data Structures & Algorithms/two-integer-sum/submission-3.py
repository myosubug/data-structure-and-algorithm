class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}


        for i, n in enumerate(nums):
            lookup[n] = i
        
        for i, n in enumerate(nums):
            if (target-n) in lookup and lookup[target-n] != i:
                return  [i, lookup[target-n]]