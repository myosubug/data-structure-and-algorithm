class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        intermediate = []
        ret = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            heapq.heappush(heap, (math.sqrt(x*x+y*y), i))

        for j in range(k):
            dist, idx = heapq.heappop(heap)
            intermediate.append(idx)

        for index in intermediate:
            ret.append(points[index])

        return ret
