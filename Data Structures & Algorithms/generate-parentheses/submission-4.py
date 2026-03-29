class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def helper(o, c, path):
            if o == n and c == n:
                ret.append("".join(path.copy()))
                return

            if o < n:
                path.append("(")
                helper(o+1, c, path)
                path.pop()
            if c < o:
                path.append(")")
                helper(o, c+1, path)
                path.pop()

        helper(0, 0, [])


        return ret