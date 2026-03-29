class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lookup = set()
        for n in nums:
            if n in lookup:
                return n
            lookup.add(n)

        return -1