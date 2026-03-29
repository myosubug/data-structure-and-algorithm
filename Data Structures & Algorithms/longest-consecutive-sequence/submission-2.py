class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for n in nums:
            streak, curr = 0, n
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)

        return res