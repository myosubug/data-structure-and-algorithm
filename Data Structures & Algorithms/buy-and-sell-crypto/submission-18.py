class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxp = 0

        while right < len(prices):
            tempp = prices[right] - prices[left]
            maxp = max(maxp, tempp)
            if tempp > 0:
                right += 1
            else:
                left = right
                right = left + 1
        

        return maxp