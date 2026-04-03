class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_profit = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[right] - prices[left] > 0:
                running_profit = max(running_profit, prices[right] - prices[left])
            else:
                left = right
                right = left + 1

        return running_profit
