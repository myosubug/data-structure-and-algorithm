class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # ret = 0

        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         cur_sub = nums[i:j+1]
        #         if cur_sub:
        #             cur_prod = math.prod(cur_sub)
        #             if cur_prod < k:
        #                 ret += 1

        # return ret

        ret = 0
        left = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            ret += (right - left + 1)
        return ret