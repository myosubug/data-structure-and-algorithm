class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxheap = []
        ret = []

        for j in count.keys():
            heapq.heappush(maxheap, (-count[j], j))

        for i in range(k):
            ret.append(heapq.heappop(maxheap)[1])

        return ret