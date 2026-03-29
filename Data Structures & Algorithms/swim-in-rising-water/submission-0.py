class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        heap = [(grid[0][0],0,0)]

        while heap:
            t, r, c = heapq.heappop(heap)
            
            if r == n-1 and c == n-1:
                return t

            if visited[r][c]:
                continue
            visited[r][c] = True

            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < n:
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
        
        return -1