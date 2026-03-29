import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for n in stones:
            heapq.heappush(heap, -n)

        while len(heap) > 1:
            a = heapq.heappop(heap) * -1
            b = heapq.heappop(heap) * -1

            if abs(a-b) != 0:
                heapq.heappush(heap, -abs(a-b))

        
        if len(heap) == 0:
            return 0
        else:
            return heap[0] * -1