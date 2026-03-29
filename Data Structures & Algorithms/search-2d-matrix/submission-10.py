class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in range(len(matrix)):
            if matrix[r][0] <= target <= matrix[r][-1]:
                return self.binarySearch(matrix[r], target)


        return False



    def binarySearch(self, nums, target):
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False