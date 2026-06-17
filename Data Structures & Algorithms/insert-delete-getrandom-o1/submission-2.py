import random

class RandomizedSet:

    def __init__(self):
        self.lookup = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.lookup:
            self.lookup[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        
        target_idx = self.lookup[val]
        target_value = val
        last_value = self.nums[-1]
        last_idx = -1

        self.nums[target_idx] = last_value
        self.nums[last_idx] = target_value
        self.nums.pop()

        self.lookup[last_value] = target_idx
        del self.lookup[val]
        

    def getRandom(self) -> int:
        return self.nums[int(random.uniform(0, len(self.nums)-1))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()