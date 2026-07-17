class MedianFinder:

    def __init__(self):
        #lower 43,2,1
        self.maxheap = []

        #upper 4,5,6,
        self.minheap = []

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
        total_len = len(self.maxheap) + len(self.minheap)
        if total_len % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            if len(self.maxheap) > len(self.minheap):
                return -self.maxheap[0]
            else:
                return self.minheap[0]
        
        