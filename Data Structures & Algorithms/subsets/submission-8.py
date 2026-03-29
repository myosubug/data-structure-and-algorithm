class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []


        def helper(idx, path):
            if idx == len(nums):
                ret.append(path.copy())
                return

            
            path.append(nums[idx])
            helper(idx+1, path)

            path.pop()
            helper(idx+1, path)

        helper(0, [])


        return ret
            