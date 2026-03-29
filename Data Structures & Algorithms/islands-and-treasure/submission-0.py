class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        queue = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append([i,j])
        
        while queue:
            popped = queue.popleft()
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nei_x = popped[0] + dx
                nei_y = popped[1] + dy
                if 0 <= nei_x < row and 0 <= nei_y < col and grid[nei_x][nei_y] == 2147483647:
                    grid[nei_x][nei_y] = grid[popped[0]][popped[1]] + 1
                    queue.append([nei_x,nei_y])


