class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == "(" or b == "{" or b == "[":
                stack.append(b)
            else:
                if stack:
                    if b == ")" and stack.pop() != "(":
                        return False
                    elif b == "]" and stack.pop() != "[":
                        return False
                    elif b == "}" and stack.pop() != "{":
                        return False
                else:
                    return False

        return True if not stack else False