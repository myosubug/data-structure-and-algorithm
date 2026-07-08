class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        ret = []

        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(minheap, (distance, (x,y)))

        for i in range(k):
            ret.append(heapq.heappop(minheap)[1])

        return ret