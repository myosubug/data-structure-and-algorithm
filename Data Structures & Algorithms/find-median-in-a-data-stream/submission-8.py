class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num >= self.minheap[0]:
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
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        else:
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            else:
                return -self.maxheap[0]