class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ret = []

        for x, y in points:
            heapq.heappush(heap, (math.sqrt(x**2+y**2),(x,y)))
        
        print(heap)

        for i in range(k):
            _, coord = heapq.heappop(heap)
            ret.append(list(coord))

        return ret