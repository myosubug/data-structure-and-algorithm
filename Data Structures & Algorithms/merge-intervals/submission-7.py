class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        left = intervals[0][0]
        right = intervals[0][1]
        ret = []

        for start, end in intervals[1:]:
            if right >= start:
                right = max(right, end)
            else:
                ret.append([left, right])
                left = start
                right = end

        ret.append([left,right])

        return ret