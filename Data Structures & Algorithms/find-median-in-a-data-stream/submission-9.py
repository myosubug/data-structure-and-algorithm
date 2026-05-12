class MedianFinder:

    def __init__(self):
        # right side
        self.minheap = []
        # left sdie
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        if len(self.minheap) > len(self.maxheap) and abs(len(self.minheap) - len(self.maxheap)) > 1:
            popped = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -popped)
        elif len(self.maxheap) > len(self.minheap) and abs(len(self.maxheap) - len(self.minheap)) > 1:
            popped = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1 * popped)


    def findMedian(self) -> float:
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0:
            return ((self.maxheap[0] * -1) + self.minheap[0]) / 2
        else:
            if len(self.maxheap) > len(self.minheap):
                return self.maxheap[0] * -1
            else:
                return self.minheap[0]
        
        