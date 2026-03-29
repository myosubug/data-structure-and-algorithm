class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n


        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
        # print(prefix)
        # print(postfix)




    #     ret = []

    #     for i, n in enumerate(nums):
    #         sliced = nums[:i]+nums[i+1:]
    #         ret.append(self.product(sliced))

    #     return ret


    # def product(self, ns):
    #     if len(ns) == 0:
    #         return 0
    #     ret = ns[0]

    #     for i in range(1, len(ns)):
    #         ret = ret * ns[i]

    #     return ret