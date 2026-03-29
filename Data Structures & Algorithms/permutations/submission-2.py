class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []


        def backtrack(i):
            if i == len(nums):
                res.append(temp.copy())
                return


            for n in nums:
                if n not in temp:
                    temp.append(n)
                    backtrack(i+1)
                    temp.pop()

        backtrack(0)


        return res
