class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for r in matrix:
    #         if self.binarySearch(r, target):
    #             return True

    #     return False

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if not (top <= bottom):
            return False

        
        m = (top + bottom) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            if target < matrix[m][mid]:
                r = mid - 1
            elif target > matrix[m][mid]:
                l = mid + 1
            else:
                return True

        return False
    


    # def binarySearch(self, nums, target):
    #     l, r = 0, len(nums)-1

    #     while l <= r:
    #         m = l + ((r-l) // 2)
    #         if target < nums[m]:
    #             r = m - 1
    #         elif target > nums[m]:
    #             l = m + 1
    #         else:
    #             return True
        
    #     return False
