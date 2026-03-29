class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ret = []

        if not newInterval:
            return intervals
        
        start, end = intervals[0][0], intervals[0][1]
        for left, right in intervals:
            if end >= left:
                end = max(end, right)
            else:
                ret.append([start,end])
                start = left
                end = right
        
        ret.append([start,end])
        return ret