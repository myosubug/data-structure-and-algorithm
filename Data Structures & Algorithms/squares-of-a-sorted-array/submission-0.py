class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        ret = []
        for n in nums:
            heapq.heappush(heap, n*n)
        

        for i in range(len(nums)):
            ret.append(heapq.heappop(heap))

        return ret