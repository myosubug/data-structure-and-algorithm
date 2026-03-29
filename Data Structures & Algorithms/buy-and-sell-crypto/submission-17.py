class Solution:
    '''
      Think of it this way:
   1. The algorithm's primary goal is to lock in the lowest possible `buying price`.
   2. Once that foundation is set, its secondary goal is to find the highest possible `selling price` that
      comes after it.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        max_p = float('-inf')
        left = 0
        right = left + 1


        while right < len(prices):
            temp_p = prices[right]-prices[left]
            if temp_p > 0:
                max_p = max(temp_p, max_p)
                right += 1
            else:
                left = right
                right = left + 1

        return max_p if max_p != float('-inf') else 0