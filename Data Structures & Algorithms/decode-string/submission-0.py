class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c != "]":
                stack.append(c)
            else:
                subs = ""
                while stack[-1] != "[":
                    subs = stack.pop() + subs
                stack.pop()

                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                stack.append(int(count) * subs)

        return "".join(stack)

