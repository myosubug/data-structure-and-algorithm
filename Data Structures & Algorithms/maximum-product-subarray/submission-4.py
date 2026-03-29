class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1, 1

        for n in nums:
            temp_max = max(n*curmin, n*curmax, n)
            curmin = min(n*curmin, n*curmax, n)
            curmax = temp_max

            res = max(curmax, res)

        return res