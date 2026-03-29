class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lookup = {}
        for n in nums:
            if n in lookup:
                return n
            else:
                lookup[n] = 1