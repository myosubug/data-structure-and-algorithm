class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed) or not flowerbed:
            return False
        
        if n == 0:
            return True
        

        if len(flowerbed) <= 2:
            if sum(flowerbed) >= 1:
                return False
            else:
                return True
        
        for i, p in enumerate(flowerbed):
            if p == 0:
                if i == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                elif i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
            if n == 0:
                return True

        return False

