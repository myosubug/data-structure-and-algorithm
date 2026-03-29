class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        heap = []
        ret = []

        for key, val in nums_count.items():
            heapq.heappush(heap, (-val,key))

        for i in range(k):
            ret.append(heapq.heappop(heap)[1])

        return ret