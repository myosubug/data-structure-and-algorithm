class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []

        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            elif c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    return False
                
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            elif c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                