class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ret = 0
        left = 0
        product = 1

        for right in range(n):
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            ret += right-left+1

        return ret