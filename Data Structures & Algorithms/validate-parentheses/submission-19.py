class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            else:
                if stack:
                    popped = stack.pop()
                    if c == "]" and popped != "[":
                        return False
                    if c == ")" and popped != "(":
                        return False
                    if c == "}" and popped != "{":
                        return False
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False