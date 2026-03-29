class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                temp = int(stack.pop()) + int(stack.pop())
                stack.append(temp)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                temp = int(stack.pop()) * int(stack.pop())
                stack.append(temp)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))

        return stack[0]   