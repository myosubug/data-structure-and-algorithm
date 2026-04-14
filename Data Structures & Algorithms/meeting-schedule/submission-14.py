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

        intervals2 = []
        for it in intervals:
            intervals2.append([it.start, it.end])
        intervals2.sort()
        s1, e1 = intervals2[0][0], intervals2[0][1]

        for s2, e2 in intervals2[1:]:
            if e1 > s2:
                return False
            s1, e1 = s2, e2

        return True