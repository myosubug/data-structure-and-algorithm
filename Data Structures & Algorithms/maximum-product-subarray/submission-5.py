class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1, 1

        for n in nums:
            curmin, curmax = min(n*curmax, n*curmin, n), max(n*curmax, n*curmin, n)

            res = max(curmax, res)

        return res