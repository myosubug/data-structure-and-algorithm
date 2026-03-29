class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force: n^2 search



        # row search
        top, bot = 0, len(matrix) -1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break

        midrow = (top + bot) // 2

        if not (top <= bot):
            return False

        # col search

        left, right = 0, len(matrix[0]) -1


        while left <= right:
            midcol = (left + right) // 2
            if matrix[midrow][midcol] < target:
                left = midcol + 1
            elif matrix[midrow][midcol] > target:
                right = midcol - 1
            else:
                return True
        

        return False