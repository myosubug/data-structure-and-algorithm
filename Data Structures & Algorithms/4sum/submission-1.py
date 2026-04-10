class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = set()

        for i in range(n):
            for j in range(i+1, n):
                left = j+1
                right = n-1
                while left < right:
                    temp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp_sum == target:
                        ret.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                        right -= 1
                    elif temp_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return list(ret)
