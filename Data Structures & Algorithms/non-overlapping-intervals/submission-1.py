class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[1])
        n = len(intervals)
        prevend = intervals[0][1]
        overlap = 0

        for i in range(1, n):
            if prevend > intervals[i][0]:
                overlap += 1
            else:
                prevend = intervals[i][1]

        return overlap

