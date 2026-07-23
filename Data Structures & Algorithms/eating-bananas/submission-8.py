class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right) // 2
            total_time = 0
            for banana in piles:
                total_time += math.ceil(float(banana)/mid)

            if total_time <= h:
                right = mid
            else:
                left = mid + 1

        return left