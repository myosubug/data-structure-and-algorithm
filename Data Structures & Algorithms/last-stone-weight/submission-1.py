class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            first, second = -heapq.heappop(heap), -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -abs(first-second))


        return 0 if len(heap) == 0 else -heap[-1]