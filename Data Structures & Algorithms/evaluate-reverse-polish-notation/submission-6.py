class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
                if c == "+":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first+second)
                elif c == "-":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first-second)
                elif c == "*":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first*second)
                elif c == "/":
                    second = stack.pop()
                    first = stack.pop()
                    div = float(first) / int(second)
                    stack.append(int(div))
                else:
                    stack.append(int(c))

        return stack[-1] if stack else 0