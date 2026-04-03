class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_sum = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[right] - prices[left] > 0:
                total_sum += prices[right] - prices[left]

            left = right
            right = left + 1

        return total_sum