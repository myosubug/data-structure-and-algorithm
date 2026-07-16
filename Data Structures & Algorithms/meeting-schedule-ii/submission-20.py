"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        interval_list = []
        for i in intervals:
            interval_list.append([i.start, i.end])

        interval_list.sort()

        heap = []
        max_rooms = 0

        for start, end in interval_list:
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            max_rooms = max(max_rooms, len(heap))

        return max_rooms