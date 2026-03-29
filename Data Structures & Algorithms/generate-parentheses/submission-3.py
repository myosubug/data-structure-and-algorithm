class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        b = []

        def helper(o, c):
            if o == n and c == n:
                ret.append("".join(b.copy()))
                return

            if o < n:
                b.append("(")
                helper(o+1, c)
                b.pop()
            if c < o:
                b.append(")")
                helper(o, c+1)
                b.pop()
            
            return


        helper(0, 0)

        return ret