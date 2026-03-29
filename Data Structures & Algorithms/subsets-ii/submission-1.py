class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        path = []

        def helper(idx):
            if idx == len(nums):
                ret.add(tuple(path.copy()))
                return

            helper(idx+1)

            path.append(nums[idx])
            helper(idx+1)
            path.pop()

        helper(0)

        return [list(s) for s in ret]