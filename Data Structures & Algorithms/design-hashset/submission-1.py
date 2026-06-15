class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]
        
    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hashed = self._hash(key)
        if key not in self.bucket[hashed]:   
            self.bucket[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = self._hash(key)
        if key in self.bucket[hashed]:   
            self.bucket[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = self._hash(key)
        if key in self.bucket[hashed]:   
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)