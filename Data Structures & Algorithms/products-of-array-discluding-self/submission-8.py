class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_sum = [1] * len(nums)
        right_sum = [1] * len(nums)
        ret = []

        for i in range(1,len(nums)):
            left_sum[i] = left_sum[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            right_sum[j] = right_sum[j+1] * nums[j+1]

        for k in range(len(nums)):
            ret.append(left_sum[k]*right_sum[k])

        return ret