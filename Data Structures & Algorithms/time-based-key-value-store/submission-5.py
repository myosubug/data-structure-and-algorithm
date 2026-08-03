class TimeMap:

    def __init__(self):
        self.lookup = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.lookup:
            self.lookup[key] = []
        self.lookup[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.lookup:
            return ""
        else:
            max_timestamp_idx = -1
            for i, v in enumerate(self.lookup[key]):
                if v[0] <= timestamp:
                    max_timestamp_idx = i
            
            if max_timestamp_idx == -1:
                return ""
            return self.lookup[key][max_timestamp_idx][1]
