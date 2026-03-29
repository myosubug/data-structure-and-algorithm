class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n-1, -1, -1):
            for j in range(amount + 1):
                dp[i][j] = dp[i+1][j]  # Don't use coin i
                if j >= coins[i]:
                    dp[i][j] += dp[i][j-coins[i]]  # Use coin i
        
        return dp[0][amount]
        

        