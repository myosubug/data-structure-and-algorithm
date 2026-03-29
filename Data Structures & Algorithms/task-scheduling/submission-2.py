class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxheap = [-c for c in counter.values()]
        heapq.heapify(maxheap)
        time = 0
        queue = deque()


        while maxheap or queue:
            time += 1
            if maxheap:
                task = heapq.heappop(maxheap)
                task += 1
                if task:
                    queue.append((task, time+n))
            if queue:
                if time == queue[0][1]:
                    heapq.heappush(maxheap, queue.popleft()[0])
        
        return time