class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()


        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                temp_sum = nums[i] + nums[l] + nums[r]
                if temp_sum == 0:
                    ret.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif temp_sum < 0:
                    l += 1
                else:
                    r -= 1
        

        return [list(i) for i in ret]
