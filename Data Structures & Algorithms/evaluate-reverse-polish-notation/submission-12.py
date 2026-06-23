class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first+second)
            
            elif c == "-":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first-second)
            elif c == "*":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first*second)
            elif c == "/":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(int(first / second))
            else:
                stack.append(int(c))

        return int(stack[-1])