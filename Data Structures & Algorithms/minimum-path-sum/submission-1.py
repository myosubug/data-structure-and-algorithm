class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[grid[0][0]] * len(grid[0]) for _ in range(len(grid))]

        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for j in range(1, len(grid[0])):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        for k in range(1, len(dp)):
            for l in range(1, len(dp[0])):
                dp[k][l] = grid[k][l] + min(dp[k-1][l], dp[k][l-1])

        return dp[-1][-1]

