class TimeMap:
    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
         
    def get(self, key: str, timestamp: int) -> str:
        res, infos = "", self.store.get(key, [])
        l, r = 0, len(infos)-1
        
        while l <= r:
            mid = (l + r) // 2
            if infos[mid][1] <= timestamp:
                res = infos[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res


'''
    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        if timestamp not in self.store[key]:
            self.store[key][timestamp] = []
        
        self.store[key][timestamp].append(value)
         
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        seen = 0

        for time in self.store[key]:
            if time <= timestamp:
                seen = max(seen, time)

        return "" if seen == 0 else self.store[key][seen][-1]
'''
        
