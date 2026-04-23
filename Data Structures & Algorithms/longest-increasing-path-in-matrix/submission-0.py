class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        indegree = [[0] * col for _ in range(row)]
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        queue = deque()

        # build indegree
        for i in range(row):
            for j in range(col):
                for dx, dy in direction:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] < matrix[i][j]:
                        indegree[i][j] += 1

        for i in range(row):
            for j in range(col):
                if indegree[i][j] == 0:
                    queue.append((i,j))

        ret = 0
        while queue:
            for _ in range(len(queue)):
                a, b = queue.popleft()
                for dx, dy in direction:
                    ni, nj = a+dx, b+dy
                    if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] > matrix[a][b]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            queue.append((ni,nj))
            ret += 1
        
        return ret
