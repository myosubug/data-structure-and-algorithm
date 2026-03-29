class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1, 1
        
        for n in nums:
            temp_max = max(n * curmax, n * curmin, n)
            curmin = min(curmax * n, curmin * n, n)
            curmax = temp_max
            
            res = max(res, curmax)

        return res