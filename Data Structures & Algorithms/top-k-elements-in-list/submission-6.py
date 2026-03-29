import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # lookup = {}
        # heap = []
        # ret = []

        # for n in nums:
        #     if n in lookup:
        #         lookup[n] += 1
        #     else:
        #         lookup[n] = 1

        # print(lookup)

        # for n, c in lookup.items():
        #     heapq.heappush(heap, (-c,n))

        # while heap and k > 0:
        #     print(heap)
        #     c, n = heapq.heappop(heap)
        #     ret.append(n)
        #     k -= 1

        # return ret

        freq = [[] for i in range(len(nums) + 1)]
        lookup = {}
        for n in nums:
            if n in lookup:
                lookup[n] += 1
            else:
                lookup[n] = 1

        for n, c in lookup.items():
            freq[c].append(n)

        ret = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret

        return ret

        