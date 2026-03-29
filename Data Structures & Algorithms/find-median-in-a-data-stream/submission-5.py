class MedianFinder:

    def __init__(self):
        # 1 2 3 4 5 6 7
        # maxheap minheap
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        if len(self.minheap) - len(self.maxheap) > 1:
            popped = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -popped)
        elif len(self.maxheap) - len(self.minheap) > 1:
            popped = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -popped)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return self.maxheap[0] * -1
        else:
            return (self.maxheap[0] * -1 + self.minheap[0]) / 2
        
        