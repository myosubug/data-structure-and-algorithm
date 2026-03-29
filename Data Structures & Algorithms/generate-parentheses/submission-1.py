class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        stack = []


        def helper(o,c):
            if o == n and c == n:
                ret.append("".join(stack))
                return
            
            if o < n:
                stack.append("(")
                helper(o+1, c)
                stack.pop()
            
            if c < o:
                stack.append(")")
                helper(o, c+1)
                stack.pop()
        
        helper(0, 0)

        return ret