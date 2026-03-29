import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1

        # nlogn solution
        # heap = []
        # for k in lookup:
        #     heapq.heappush(heap, (-lookup[k], k))
        # ret = []

        # for i in range(k):
        #     c = heapq.heappop(heap)
        #     print(heap)
        #     ret.append(c[1])
        #     print(ret)

        for n, c in lookup.items():
            freq[c].append(n)

        ret = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret
        
        return ret

        return ret
        