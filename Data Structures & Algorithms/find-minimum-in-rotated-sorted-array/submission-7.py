class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        ret = float('inf')


        while left <= right:
            mid = (left + right) // 2
            ret = min(nums[mid], ret)
            
            if nums[mid] > nums[right]:
                # [4, 5, 6, 1, 2, 3]
                left = mid + 1
            else:
                right = mid - 1
        

        return ret
            
