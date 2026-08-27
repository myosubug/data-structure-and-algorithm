class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        ret = []

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        for j in range(n-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]

        for k in range(n):
            ret.append(left[k]*right[k])

        return ret
