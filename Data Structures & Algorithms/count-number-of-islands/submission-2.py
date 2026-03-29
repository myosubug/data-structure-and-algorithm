class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, row, col, grid)

        return count


    def dfs(self, i, j, row, col, grid):
        if not (0 <= i < row) or not (0 <= j < col) or grid[i][j] != "1":
            return

        grid[i][j] = "$"

        self.dfs(i+1, j, row, col, grid)
        self.dfs(i-1, j, row, col, grid)
        self.dfs(i, j+1, row, col, grid)
        self.dfs(i, j-1, row, col, grid)
