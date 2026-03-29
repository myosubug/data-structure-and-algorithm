class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        left, right = intervals[0][0], intervals[0][1]


        for start, end in intervals[1:]:
            if start <= right:
                right = max(right, end)
            else:
                ret.append([left,right])
                left, right = start, end

        ret.append([left,right])


        return ret
            