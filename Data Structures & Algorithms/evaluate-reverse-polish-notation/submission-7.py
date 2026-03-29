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


'''
   11     def apply_op():
   12         """Applies the top operator to the top two values."""
   13         operator = ops.pop()
   14         right = values.pop()
   15         left = values.pop()
   16 
   17         if operator == '+': values.append(left + right)
   18         elif operator == '-': values.append(left - right)
   19         elif operator == '*': values.append(left * right)
   20         elif operator == '/': values.append(int(left / right))
   21 
   22     for token in tokens:
   23         # If it's a number (including negative), push to values stack
   24         if token.lstrip('-').isdigit():
   25             values.append(int(token))
   26 
   27         # If it's an opening parenthesis, push to operators stack
   28         elif token == '(':
   29             ops.append(token)
   30 
   31         # If it's a closing parenthesis, solve everything inside
   32         elif token == ')':
   33             while ops[-1] != '(':
   34                 apply_op()
   35             ops.pop()  # Discard the '('
   36 
   37         # Otherwise, it's an operator
   38         else:
   39             # Before pushing, apply any operators with higher or equal precedence
   40             while ops and ops[-1] != '(' and precedence.get(ops[-1]) >= precedence[token]:
   41                 apply_op()
   42             ops.append(token)
   43 
   44     # Apply any remaining operators
   45     while ops:
   46         apply_op()
   47 
   48     return values[0]
'''