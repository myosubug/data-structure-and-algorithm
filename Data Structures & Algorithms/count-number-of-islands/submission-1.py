class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = grid.copy()
        count = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if visited[i][j] == "1":
                    count += 1
                    self.dfs(i,j,row,col,visited)

        
        return count


    def dfs(self, i, j, row, col, visited):
        if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] == "0" or visited[i][j] == "$":
            return
    
        visited[i][j] = "$"

        self.dfs(i+1,j,row,col,visited)
        self.dfs(i,j+1,row,col,visited)
        self.dfs(i-1,j,row,col,visited)
        self.dfs(i,j-1,row,col,visited)