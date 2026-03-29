class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    ret += 1
                    self.helper(i, j, row, col, grid)

        return ret
    
    def helper(self, i, j, row, col, grid):
        if not (0 <= i < row) or not (0 <= j < col) or grid[i][j] != "1":
            return

        grid[i][j] = "$"

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            self.helper(i+dx, j+dy, row, col, grid)
        