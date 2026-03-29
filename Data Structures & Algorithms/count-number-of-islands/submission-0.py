class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = grid.copy()
        # iterate i, j of grid
        # if starts or stuck on 0, skip, don't count as island
        # if starts on stuck on visited, skip, don't count as island
        # if starts on 1, start counting + 1 and mark all visited 1s as $
        ROW = len(grid)
        COL = len(grid[0])
        counter = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and visited [i][j] != "$":
                    counter += 1
                    self.search(i, j, visited, ROW, COL)
                    
        
        return counter

    def search(self, i, j, visited, ROW, COL):
        if i >= ROW or i < 0 or j >= COL or j < 0 or visited[i][j] == "0" or visited[i][j] =="$":
            return

        visited[i][j] = "$"
        
        self.search(i+1, j, visited, ROW, COL)
        self.search(i-1, j, visited, ROW, COL)
        self.search(i, j+1, visited, ROW, COL)
        self.search(i, j-1, visited, ROW, COL)
