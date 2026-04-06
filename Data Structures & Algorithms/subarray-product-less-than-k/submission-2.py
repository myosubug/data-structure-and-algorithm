class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        left = 0
        prod = 1

        for right in range(n):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod = prod // nums[left]
                left += 1
            ret += right-left+1

        return ret