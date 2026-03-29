class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        cache = [0] * (n+1)
        cache[0] = 0
        cache[1] = 1
        cache[2] = 2
        cache[3] = 3

        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]