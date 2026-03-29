class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [i for i in range(n+1)]

        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        
        return cache[n]