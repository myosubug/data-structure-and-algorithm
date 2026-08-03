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
            arr = self.lookup[key]
            left, right = 0, len(arr)-1
            res = ""
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] <= timestamp:
                    res = arr[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1

            return res
