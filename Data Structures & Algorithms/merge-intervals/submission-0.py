class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []

        start, end = intervals[0][0], intervals[0][1]

        for left, right in intervals:
            if end >= left:
                end = max(end, right)
            else:
                ret.append([start, end])
                start, end = left, right

        ret.append([start, end])


        return ret