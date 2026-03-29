class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []

        def helper(path, usage_check):
            if len(path) == len(nums):
                ret.append(path.copy())
                return

            for i, n in enumerate(nums):
                if not usage_check[i]:
                    path.append(n)
                    usage_check[i] = True
                    helper(path, usage_check)
                    path.pop()
                    usage_check[i] = False
        
        helper([], [False]*len(nums))

        return ret
            
