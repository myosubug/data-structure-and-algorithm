class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        top, bot = 0, row-1

        while top <= bot:
            if target > matrix[top][-1]:
                top += 1
            elif target < matrix[bot][0]:
                bot -= 1
            else:
                break
        
        if not (top <= bot):
            return False

        left, right = 0, col-1

        while left <= right:
            mid_idx = (left + right) // 2
            mid_val = matrix[top][mid_idx]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        
        return False

