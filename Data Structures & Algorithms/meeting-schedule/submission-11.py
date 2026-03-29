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

        trans = []

        for iv in intervals:
            trans.append([iv.start, iv.end])

        trans.sort()
        left, right = trans[0][0], trans[0][1]

        for left2, right2 in trans[1:]:
            if right > left2:
                return False
            left, right = left2, right2

        return True