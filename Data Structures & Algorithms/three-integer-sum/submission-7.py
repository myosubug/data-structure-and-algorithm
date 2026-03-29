class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i-1] == n:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                temp_sum = n + nums[left] + nums[right]
                if temp_sum == 0:
                    ret.append([n,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif temp_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return ret
