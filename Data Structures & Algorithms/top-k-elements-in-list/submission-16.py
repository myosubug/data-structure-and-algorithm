class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        ret = []

        for key, v in count.items():
            heapq.heappush(heap, (-v, key))


        for i in range(k):
            value, popped_key = heapq.heappop(heap)
            ret.append(popped_key)

        return ret