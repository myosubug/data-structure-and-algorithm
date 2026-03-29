class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            else:
                if stack:
                    popped = stack.pop()
                    if popped == "[" and c != "]":
                        return False
                    elif popped == "(" and c != ")":
                        return False
                    elif popped == "{" and c != "}":
                        return False
                else:
                    return False
        
        return True if not stack else False