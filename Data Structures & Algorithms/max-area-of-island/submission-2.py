class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = grid.copy()
        row, col = len(grid), len(grid[0])
        counter = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] != -1:
                    temp_count = self.search(i, j, row, col, visited)
                    counter = max(counter, temp_count)

        return counter


    def search(self, i, j, r, c, visited):
        if i < 0 or i >= r or j < 0 or j >= c or visited[i][j] == -1 or visited[i][j] == 0:
            return 0

        visited[i][j] = -1

        return 1 + self.search(i+1,j,r,c,visited) + self.search(i-1,j,r,c,visited) + self.search(i,j+1,r,c,visited) + self.search(i,j-1,r,c,visited)
