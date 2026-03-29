class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        row, col = len(grid), len(grid[0])
        visited = set()
        origin = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    origin.append((i,j))
        
        if fresh == 0:
            return 0
        
        time = 0
        while origin:
            if fresh <= 0:
                break
            time += 1
            for _ in range(len(origin)):
                px, py = origin.popleft()
                for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    cx,cy = px+dx, py+dy
                    if 0 <= cx < row and 0 <= cy < col and (cx,cy) not in visited and grid[cx][cy] == 1:
                        grid[cx][cy] = 2
                        visited.add((cx,cy))
                        origin.append((cx,cy))
                        fresh -= 1

        
        return time if fresh == 0 else -1