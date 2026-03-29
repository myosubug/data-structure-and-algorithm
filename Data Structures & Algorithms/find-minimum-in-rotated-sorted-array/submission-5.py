class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        minimum = float('inf')

        while left < right:
            mid = (left + right) // 2
            minimum = min(nums[mid], minimum)

            if nums[mid] > nums[right]:
                # 3 4 5 1 2
                left = mid + 1
            else:
                # 1 2 3 4 5
                right = mid - 1
        
        
        return min(minimum, nums[(left+right)//2])