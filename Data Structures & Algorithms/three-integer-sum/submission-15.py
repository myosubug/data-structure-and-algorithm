class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum == 0:
                    ret.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif temp_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return ret