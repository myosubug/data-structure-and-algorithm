class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp_area = self.helper(i, j, row, col, grid)
                    max_area = max(max_area, temp_area)

        return max_area

    def helper(self, i, j, row, col, grid):
        if not (0 <= i < row) or not (0 <= j < col):
            return 0
        if grid[i][j] != 1:
            return 0
        
        counter = 1
        grid[i][j] = 0
        
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            counter += self.helper(i+dx, j+dy, row, col, grid)
        
        return counter