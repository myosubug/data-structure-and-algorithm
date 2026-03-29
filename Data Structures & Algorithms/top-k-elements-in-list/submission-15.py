class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        heap = []
        ret = []


        for key in num_counter.keys():
            heapq.heappush(heap, (-num_counter[key], key))


        for i in range(k):
            val, key = heapq.heappop(heap)
            ret.append(key)


        return ret