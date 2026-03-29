class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxp = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                maxp = max(maxp, prices[right]-prices[left])
                right += 1
            else:
                left = right
                right = left + 1
            
        
        return maxp