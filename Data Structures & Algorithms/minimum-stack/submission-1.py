class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if len(self.stack) > 0:
            if val < self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.minstack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()


    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:
        print(self.minstack)
        print(self.stack)
        return self.minstack[-1]
