class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]

        for start2, end2 in intervals[1:]:
            if end >= start2:
                start = min(start, start2)
                end = max(end, end2)
            else:
                ret.append([start,end])
                start = start2
                end = end2
        
        ret.append([start,end])


        return ret