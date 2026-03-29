class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lookup = set(nums)

        for i in range(len(nums)+1):
            if i not in lookup:
                return i
        
