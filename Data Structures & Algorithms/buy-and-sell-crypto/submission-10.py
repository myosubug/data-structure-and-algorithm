class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        left = 0
        right = left + 1

        while right < len(prices):
            if prices[right] - prices[left] > 0:
                max_p = max(max_p, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right = left + 1

        return max_p