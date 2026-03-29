class Solution:

    def climbStairs(self, n: int) -> int:
        self.memo = {}

        def recur(n):
            if n in self.memo:
                return self.memo[n]
        
            if n <= 3:
                ret = n
            else:
                ret = recur(n-1) + recur(n-2)

            self.memo[n] = ret

            return ret

        res = recur(n)
        
        return res
        