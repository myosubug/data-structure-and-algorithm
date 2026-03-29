class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = grid.copy()
        ROW, COL = len(grid), len(grid[0])
        max_area = 0

        def search(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or visited[i][j] == 0 or visited[i][j] == -1:
                return 0 

            visited[i][j] = -1
            
            return 1 + search(i+1, j) + search(i-1, j) + search(i, j+1) + search(i, j-1)

        for i in range(ROW):
            for j in range(COL):
                if visited[i][j] == 1 and visited[i][j] != -1:
                    max_area = max(max_area, search(i,j))
                    

        return max_area

    
        