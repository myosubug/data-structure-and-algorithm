class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if t == "+":
                second = nums.pop()
                first = nums.pop()
                nums.append(int(first+second))
            elif t == "-":
                second, first = nums.pop(), nums.pop()
                nums.append(first-second)
            elif t == "*":
                second = nums.pop()
                first = nums.pop()
                nums.append(first*second)
            elif t == "/":
                second = nums.pop()
                first = nums.pop()
                nums.append(math.trunc(first/second))
            else:
                nums.append(int(t))

        return nums[-1]