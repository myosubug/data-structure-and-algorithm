class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        flipped = None
        if x < 0:
            isNegative = True

        if isNegative:
            flipped = int((str(x)[1:])[::-1]) 
        else:
            flipped = int(str(x)[::-1])

        if isNegative:
            flipped *= -1
        
        return flipped if math.pow(-2, 31) <= flipped <= math.pow(2, 31)-1 else 0