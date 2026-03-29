class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        temp = []

        def helper(i):
            if i == len(nums):
                ret.append(temp.copy())
                return


            for n in nums:
                if n not in temp:
                    temp.append(n)
                    helper(i+1)
                    temp.pop()
        
        helper(0)
        return ret