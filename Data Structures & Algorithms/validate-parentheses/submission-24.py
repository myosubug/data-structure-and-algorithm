class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            else:
                if stack:
                    popped = stack.pop()
                    if (c == "}" and popped != "{") or (c == "]" and popped != "[") or (c == ")" and popped != "("):
                        return False
                else:
                     return False
        
        return len(stack) == 0