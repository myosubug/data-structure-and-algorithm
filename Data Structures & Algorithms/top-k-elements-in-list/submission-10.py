class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        ret = []
        for j in count.keys():
            heapq.heappush(heap, (-count[j], j))

        for i in range(k):
            ret.append(heapq.heappop(heap)[1])

        return ret