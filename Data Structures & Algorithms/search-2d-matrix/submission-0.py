class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if self.binarySearch(r, target):
                return True

        return False
    


    def binarySearch(self, nums, target):
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + ((r-l) // 2)
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return True
        
        return False