class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in lookup:
                return [lookup[diff], index]
            lookup[val] = index

