class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj_list[i].append((dist, j))
                adj_list[j].append((dist, i))

        res = 0
        visited = set()
        minheap = [(0, 0)]

        while len(visited) < n:
            cost, node = heapq.heappop(minheap)
            if node in visited:
                continue
            res += cost
            visited.add(node)

            for nei_cost, nei in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (nei_cost, nei))

        return res