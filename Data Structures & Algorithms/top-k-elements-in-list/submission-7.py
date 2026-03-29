class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = defaultdict(int)
        heap = []
        ret = []

        for n in nums:
            lookup[n] -= 1

        for key, value in lookup.items():
            heapq.heappush(heap, (value, key))

        for i in range(k):
            count, num = heapq.heappop(heap)
            ret.append(num)

        return ret