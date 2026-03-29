class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ret = 1
        lookup = set(nums)

        for n in nums:
            if n-1 not in lookup:
                temp = n
                streak = 0
                while temp in lookup:
                    temp += 1
                    streak += 1
            
                ret = max(ret, streak)

        return ret
