class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    self.update(i,j,row,col,grid)


        return count

    def update(self, i, j, row, col, grid):
        if not(0 <= i < row) or not (0 <= j < col) or grid[i][j] == "$" or grid[i][j] == "0":
            return 
        
        grid[i][j] = "$"

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            self.update(i+dx, j+dy, row, col, grid)
