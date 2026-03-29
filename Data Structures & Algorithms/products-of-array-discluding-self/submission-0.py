class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []

        for i, n in enumerate(nums):
            sliced = nums[:i]+nums[i+1:]
            ret.append(self.product(sliced))

        return ret


    def product(self, ns):
        if len(ns) == 0:
            return 0
        ret = ns[0]

        for i in range(1, len(ns)):
            ret = ret * ns[i]

        return ret