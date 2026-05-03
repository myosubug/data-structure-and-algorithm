# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.binary_search(n)
    
    def binary_search(self, rng):
        left, right = 0, rng
        while left <= right:
            mid = left + (right-left) // 2
            print(mid)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
                

        return left


        