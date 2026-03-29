class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while r < len(prices):
            tempp = prices[r] - prices[l]
            if tempp > 0:
                maxp = max(maxp, tempp)
                r += 1
            else:
                l = r
                r = l + 1
        
        return maxp