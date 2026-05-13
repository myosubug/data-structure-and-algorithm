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

        '''
        Example: [(0,40),(5,10),(15,20)]

        Meeting 1 (0,40): heap = [40]
        Meeting 2 (5,10): Is 40 ≤ 5? No. Need new room. heap = [40, 10]
        Meeting 3 (15,20): Is 10 ≤ 15? Yes! Reuse that room. heap = [40, 20]
        Answer: 2 rooms
        '''
        for s, e in trans:
            if minheap and minheap[0] <= s:
                heapq.heappop(minheap)
            heapq.heappush(minheap, e)

        return len(minheap)
