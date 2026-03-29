class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ret = []
        lookup = Counter(nums)
        for key, val in lookup.items():
            heapq.heappush(heap, (-val,key))

        for i in range(k):
            val, key = heapq.heappop(heap)
            ret.append(key)

        return ret