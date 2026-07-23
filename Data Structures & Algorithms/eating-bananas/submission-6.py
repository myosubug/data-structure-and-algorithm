class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            tt = 0
            mid = (left + right) // 2
            for b in piles:
                tt += math.ceil(float(b)/mid)
            
            if tt <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
