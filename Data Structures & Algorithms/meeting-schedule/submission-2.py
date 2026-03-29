"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # end of first item > start of the 2nd item -> false
        intervals.sort(key=lambda i:i.start)


        if not intervals or len(intervals) == 1:
            return True

        prev_start = intervals[0].start 
        prev_end = intervals[0].end 

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i].start, intervals[i].end
            if prev_end > cur_start:
                return False
            else:
                prev_start, prev_end = cur_start, cur_end

        return True
