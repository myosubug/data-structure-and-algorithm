class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        graph = [[0 for col in range(n)] for row in range(m)]

        for i in range(m):
            graph[i][0] = 1
        
        for j in range(n):
            graph[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                graph[i][j] = graph[i-1][j] + graph[i][j-1]

        
        return graph[-1][-1]