class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {i: [] for i in range(n)}
        heap = [(0, 0, src)]
        visited = set()

        for fr, to, pr in flights:
            adj_list[fr].append((pr, to))

        while heap:
            price, stop, node = heapq.heappop(heap)
            if node == dst:
                return price
            if stop > k or (node, stop) in visited:
                continue
            
            visited.add((node, stop))

            for p, t in adj_list.get(node, []):
                heapq.heappush(heap, (price+p, stop+1, t))
        
        return -1