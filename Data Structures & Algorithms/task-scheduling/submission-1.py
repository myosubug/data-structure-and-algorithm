class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # intuition
        # the more frequent task is the way to maximize idle time
        # use example 

        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)
        
        time = 0
        q = deque()


        while maxheap or q:
            time += 1
            if maxheap:
                c = 1 + heapq.heappop(maxheap)
                if c:
                    q.append([c, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])


        return time