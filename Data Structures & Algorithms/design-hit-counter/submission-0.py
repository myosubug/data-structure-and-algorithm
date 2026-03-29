class HitCounter:

    def __init__(self):
        self.timestamp = {}
        self.current_time = 0
        

    def hit(self, timestamp: int) -> None:
        if timestamp in self.timestamp:
            self.timestamp[timestamp] += 1
        else:
            self.timestamp[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        count_start = max(0, timestamp-300)
        temp_counter = 0
        for key in self.timestamp.keys():
            if count_start < key <= timestamp:
                temp_counter += self.timestamp[key]
        

        return temp_counter
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
