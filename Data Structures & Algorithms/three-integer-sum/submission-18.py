class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lookup = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    lookup.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    right -= 1
        
        ret = []

        for l in lookup:
            ret.append(list(l))

        return ret