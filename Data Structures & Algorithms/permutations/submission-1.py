class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res, p = [], []


        def backtrack():
            if len(p) == n:
                res.append(p.copy())
                return

            for x in nums:
                if x not in p:
                    p.append(x)
                    backtrack()
                    p.pop()

        backtrack()

        return res