class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ret = 0
        intervals.sort()
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                ret += 1
                # When two intervals do overlap, you need to remove one.
                prev_end = min(prev_end, end)

        return ret

