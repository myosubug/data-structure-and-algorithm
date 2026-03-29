class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ret = []
        i = 0

        #check if existing intervals are left of new interval or not
        # if yes, then add existing first if they are not overlapping
        while i < n and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i += 1

        # after adding all left intervals,
        # check if new interval is left of the next interval or not
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ret.append(newInterval)

        while i < n:
            ret.append(intervals[i])
            i += 1

        return ret

