class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while l < r and r < len(prices):
            temp = prices[r] - prices[l]
            print(temp)
            if temp >= 0:
                maxp = max(maxp, temp)
                r += 1
            else:
                l = r
                r = l + 1

        return maxp