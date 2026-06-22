class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1

        while right < len(prices):
            temp = prices[right] - prices[left]
            if temp > 0:
                max_profit = max(max_profit, temp)
                right += 1
            else:
                left = right
                right = left + 1

        return max_profit
