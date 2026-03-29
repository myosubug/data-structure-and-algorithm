class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {i: [] for i in range(n)}
        heap = [(0, 0, src)]
        visited = set()
        for frm, to, price in flights:
            adj_list[frm].append((price, to))
        while heap:
            price, stops, node = heapq.heappop(heap)
            if node == dst:
                return price
            if stops > k or (node, stops) in visited:
                continue
            visited.add((node,stops))
            
            for p, nei in adj_list.get(node, []):
                heapq.heappush(heap, (price + p, stops + 1, nei))

        return -1