class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret_set = set()

        for i in range(len(nums)):
            left = i + 1
            if left >= len(nums):
                break
            right = len(nums) - 1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum == 0:
                    ret_set.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        ret = []
        for v in ret_set:
            ret.append(list(v))

        return ret
