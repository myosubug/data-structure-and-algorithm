class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][0] <= newInterval[0]:
            i += 1
        
        intervals.insert(i, newInterval)

        s1, e1 = intervals[0]

        for s2, e2 in intervals[1:]:
            if e1 >= s2:
                s1 = min(s1, s2)
                e1 = max(e1, e2)
            else:
                ret.append([s1, e1])
                s1 = s2
                e1 = e2

        ret.append([s1, e1])

        return ret
        
