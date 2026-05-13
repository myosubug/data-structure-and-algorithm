"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        inters = []
        for ii in intervals:
            inters.append([ii.start,ii.end])


        inters.sort()
        s1, e1 = inters[0]

        for s2, e2 in inters[1:]:
            if s2 < e1:
                return False
            else:
                s1 = s2
                e1 = e2

        return True