class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)
        ret = [1] * len(nums)

        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            rightProduct[j] = rightProduct[j+1] * nums[j+1]

        for k in range(len(nums)):
            ret[k] = leftProduct[k] * rightProduct[k]

        return ret