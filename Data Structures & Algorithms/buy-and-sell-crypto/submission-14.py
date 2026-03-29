class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        left, right = 0, 1

        while right < len(prices):
            temp = prices[right]-prices[left]
            if temp <= 0:
                left += 1
                right = left + 1
            else:
                max_p = max(max_p, temp)
                right += 1
        
        return max_p