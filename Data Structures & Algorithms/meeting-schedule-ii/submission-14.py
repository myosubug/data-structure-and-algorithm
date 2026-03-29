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

        trans = []

        for iv in intervals:
            trans.append([iv.start, iv.end])

        trans.sort()
        minheap = []

        for m in trans:
            if minheap and minheap[0] <= m[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, m[1])

        return len(minheap)
        # for left, right in trans:
        #     if minheap and minheap[0] <= 
