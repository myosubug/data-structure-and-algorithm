class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp_count = self.helper(row, col, i, j, grid)
                    ret = max(ret, temp_count)

        return ret
    

    def helper(self, row, col, i, j, grid):
        if not(0 <= i < row) or not (0 <= j < col) or grid[i][j] != 1:
            return 0
        
        grid[i][j] = -1

        left = self.helper(row, col, i+1, j, grid)
        right = self.helper(row, col, i, j+1, grid)
        top = self.helper(row, col, i-1, j, grid)
        bottom = self.helper(row, col, i, j-1, grid)

        return 1 + left + right + top + bottom