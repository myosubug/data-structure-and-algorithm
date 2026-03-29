class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            elif c == "]":
                if stack:
                    popped = stack.pop()
                    if popped !="[":
                        return False
                else:
                    return False
            elif c == ")":
                if stack:
                    popped = stack.pop()
                    if popped !="(":
                        return False
                else:
                    return False
            elif c == "}":
                if stack:
                    popped = stack.pop()
                    if popped !="{":
                        return False
                else:
                    return False

        
        return True if not stack else False