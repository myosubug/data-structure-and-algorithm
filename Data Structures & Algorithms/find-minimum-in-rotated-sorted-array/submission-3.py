class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        cur_min = float('inf')

        while left <= right:
            mid = (left + right) // 2
            cur_min = min(cur_min, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1


        return min(cur_min, nums[(left+right)//2])