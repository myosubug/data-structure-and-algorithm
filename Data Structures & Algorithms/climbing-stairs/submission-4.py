class Solution:
    def climbStairs(self, n: int) -> int:
        
        lookup = [1] * (n+1)

        for i in range(2,n+1):
            lookup[i]=lookup[i-1]+lookup[i-2]

        return lookup[n]    

                               