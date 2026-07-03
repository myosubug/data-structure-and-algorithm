class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for s in stones:
            heapq.heappush(maxheap, -s)

        while len(maxheap) >= 2:
            first = heapq.heappop(maxheap) * -1
            second = heapq.heappop(maxheap) * -1
            if first > second:
                diff = first-second
                heapq.heappush(maxheap, -diff)
            elif first < second:
                diff = second-first
                heapq.heappush(maxheap, -diff)
            else:
                continue

        return -maxheap[0] if len(maxheap) == 1 else 0