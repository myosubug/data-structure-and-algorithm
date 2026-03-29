class MedianFinder:

    def __init__(self):
        self.large_minheap = []
        self.small_maxheap = []
        

    def addNum(self, num: int) -> None:
        if self.large_minheap and num > self.large_minheap[0]:
            heapq.heappush(self.large_minheap, num)
        else:
            heapq.heappush(self.small_maxheap, -num)
        
        if len(self.large_minheap) - len(self.small_maxheap) > 1:
            popped = heapq.heappop(self.large_minheap)
            heapq.heappush(self.small_maxheap, -popped)
        if len(self.small_maxheap) - len(self.large_minheap) > 1:
            popped = -heapq.heappop(self.small_maxheap)
            heapq.heappush(self.large_minheap, popped)

    def findMedian(self) -> float:
        if  len(self.small_maxheap) > len(self.large_minheap):
            return -(self.small_maxheap[0])
        elif len(self.small_maxheap) < len(self.large_minheap):
            return self.large_minheap[0]
        else:
            return (-(self.small_maxheap[0]) + self.large_minheap[0]) / 2.0
        
        