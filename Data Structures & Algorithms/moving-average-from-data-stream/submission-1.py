class MovingAverage:

    def __init__(self, size: int):
        self.temp_sum = 0
        self.nums = deque([])
        self.size = size

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.temp_sum += val
        if len(self.nums) > self.size:
            self.temp_sum -= self.nums[0]
            self.nums.popleft()
        

        return self.temp_sum / len(self.nums)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
