class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)
        time = 0
        queue = deque()

        while maxheap or queue:
            time += 1

            if maxheap:
                t = 1 + heapq.heappop(maxheap)
                if t:
                    queue.append((time+n, t))
            
            if queue:
                if time == queue[0][0]:
                    heapq.heappush(maxheap, queue.popleft()[1])

        
        return time