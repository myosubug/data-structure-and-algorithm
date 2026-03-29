class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append([i,j])
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                px, py = queue.popleft()
                dist = grid[px][py]
                for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nei_x = px + dx
                    nei_y = py + dy
                    if 0 <= nei_x < row and 0 <= nei_y < col and grid[nei_x][nei_y] == 2147483647:
                        grid[nei_x][nei_y] = dist + 1
                        queue.append([nei_x,nei_y])


