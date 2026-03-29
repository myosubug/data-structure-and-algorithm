class Solution:
    def isValid(self, s: str) -> bool:
        # the string length has to be even number to contain the 
        # valid number of parentheses
        stack = []
        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            elif p == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif p == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif p == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
        

        return len(stack) == 0