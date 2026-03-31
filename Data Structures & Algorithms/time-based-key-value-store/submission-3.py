class TimeMap:

    def __init__(self):
        self.lookup = {}
        self.timestamp_lookup = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.lookup:
            self.lookup[key] = {}
            self.timestamp_lookup[key] = []
        self.lookup[key][timestamp] = value
        self.timestamp_lookup[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.lookup:
            if timestamp in self.lookup[key]:
                return self.lookup[key][timestamp]
            else:
                most_recent_previous_timestamp = self.binary_search(self.timestamp_lookup[key], timestamp)
                return self.lookup[key].get(most_recent_previous_timestamp,"")
        else:
            return ""

    def binary_search(self, arr, target):
        left, right = 0, len(arr)-1
        ret = 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                ret = arr[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ret
