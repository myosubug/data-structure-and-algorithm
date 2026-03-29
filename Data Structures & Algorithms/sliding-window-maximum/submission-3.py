class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute
        # ret = []
        # left = 0
        # right = left + k


        # while right <= len(nums):
        #     temp = nums[left:right]
        #     ret.append(max(temp))
        #     left += 1
        #     right += 1
        
        # return ret

        ### heap

        ret = []
        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (-n,i))
            if i >= k-1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                ret.append(-heap[0][0])

        return ret

            
        