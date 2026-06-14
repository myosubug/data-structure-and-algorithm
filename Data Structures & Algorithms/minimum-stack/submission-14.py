class MinStack:

    def __init__(self):
        self.log = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.log:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1], val))

        self.log.append(val)

    def pop(self) -> None:
        self.log.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.log[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
