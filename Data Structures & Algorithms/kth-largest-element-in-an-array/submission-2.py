class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        ret = 0

        for n in nums:
            heapq.heappush(heap, -n)

        for i in range(k):
            ret = heapq.heappop(heap)

        
        return -ret