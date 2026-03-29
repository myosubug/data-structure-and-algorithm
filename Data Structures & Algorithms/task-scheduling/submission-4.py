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
                occurence = 1 + heapq.heappop(maxheap)
                if occurence < 0:
                    queue.append((occurence, time+n))

            if queue:
                if time == queue[0][1]:
                    heapq.heappush(maxheap, queue.popleft()[0])

        return time