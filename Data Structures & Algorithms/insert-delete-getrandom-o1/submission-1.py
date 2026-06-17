import random

class RandomizedSet:

    def __init__(self):
        self.lookup = {}

    def insert(self, val: int) -> bool:
        if val not in self.lookup:
            self.lookup[val] = True
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        del self.lookup[val]
        

    def getRandom(self) -> int:
        candidates = list(self.lookup.keys())
        return candidates[int(random.uniform(0, len(candidates)-1))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()