class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ret = []

        num_count = Counter(nums)

        for key in num_count:
            heapq.heappush(heap, (-num_count[key], key))
        

        for i in range (k):
            ret.append(heapq.heappop(heap)[1])

        return ret