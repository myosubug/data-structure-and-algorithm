class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # while True:
        #     tt = 0
        #     for pile in piles:
        #         tt += math.ceil(pile/speed)
        #     if tt <= h:
        #         return speed
            
        #     speed += 1
        
        # return speed


        left, right = 1, max(piles)

        while left < right:
            tt = 0
            mid = (left + right) // 2
            for pile in piles:
                tt += math.ceil(pile/ mid)

            if tt <= h:
                right = mid
            else:
                left = mid + 1
        
        return left