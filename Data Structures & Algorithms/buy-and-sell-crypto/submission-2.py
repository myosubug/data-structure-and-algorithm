class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            temp_profit = prices[r] - prices[l]
            if temp_profit < 0:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, temp_profit)
                r += 1
            print(max_profit)
        

        return max_profit