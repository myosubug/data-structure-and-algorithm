class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def helper(path, used):
            if len(path) == len(nums):
                ret.append(path.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    helper(path, used)
                    path.pop()
                    used[i] = False

        helper([], [False]*len(nums))

        return ret
