class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        if len(self.minheap) > 0 and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        if len(self.minheap)-len(self.maxheap) > 1:
            popped = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -popped)
        elif len(self.maxheap)-len(self.minheap) > 1:
            popped = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -popped)



    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]
        
        