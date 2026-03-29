class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False

        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            elif b == "]":
                if len(stack) > 0: 
                    popped = stack.pop()
                    if popped != "[":
                        return False
                else:
                    return False
            elif b == ")":
                if len(stack) > 0:
                    popped = stack.pop()
                    if popped != "(":
                        return False
                else:
                    return False
            elif b == "}":
                if len(stack) > 0:
                    popped = stack.pop()
                    if popped != "{":
                        return False
                else:
                    return False

        
        if len(stack) > 0:
            return False
        else:
            return True

