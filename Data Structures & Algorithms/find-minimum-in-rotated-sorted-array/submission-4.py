class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        current_min = float('inf')

        while left <= right:
            mid = (left + right) // 2
            current_min = min(current_min, nums[mid])

            if nums[mid] > nums[right]:
                # 3 4 5 1 2
                left = mid + 1
            else:
                # 1 2 3 4 5
                right = mid - 1
            
        
        return min(current_min, nums[(left+right) //2 ])
