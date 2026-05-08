class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b == "[" or b == "{" or b == "(":
                stack.append(b)
            else:
                if stack:
                    popped = stack.pop()
                    if b == "]":
                        if popped != "[":
                            return False
                    elif b == "}":
                        if popped != "{":
                            return False
                    elif b == ")":
                        if popped != "(":
                            return False
                else:
                    return False
        return False if stack else True