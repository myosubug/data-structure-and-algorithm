class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.cur_sum = 0
        self.cap = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.cur_sum += val
        if len(self.queue) > self.cap:
            removing = self.queue.popleft()
            self.cur_sum -= removing
        
        return self.cur_sum / len(self.queue)
        




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
