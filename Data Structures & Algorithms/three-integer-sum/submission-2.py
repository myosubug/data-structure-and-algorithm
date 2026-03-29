class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum == 0:
                    ret.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                    right -= 1
        

        return [list(t) for t in ret]
            