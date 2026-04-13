class MinStack:

    def __init__(self):
        self.minstack = []
        self.snapshot = []
        

    def push(self, val: int) -> None:
        self.snapshot.append(val)
        if self.minstack:
            self.minstack.append(min(self.minstack[-1],val))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.snapshot.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.snapshot[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
