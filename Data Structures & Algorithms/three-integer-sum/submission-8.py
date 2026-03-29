class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                temp_sum = n + nums[l] + nums[r]
                if temp_sum == 0:
                    ret.append([n,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                elif temp_sum < 0:
                    l += 1
                else:
                    r -= 1
                

        return ret