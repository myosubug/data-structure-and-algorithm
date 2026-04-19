class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj_list = {i: [] for i in range(n)}
        for i in range(n):
            x, y = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2-x) + abs(y2-y)
                adj_list[i].append((dist, j))
                adj_list[j].append((dist, i))

        minheap = [(0,0)]
        visited = set()
        min_cost = 0

        while len(visited) < n:
            dist, node = heapq.heappop(minheap)
            if node in visited:
                continue
            min_cost += dist
            visited.add(node)

            for nei_dist, nei in adj_list.get(node, []):
                if nei not in visited:
                    heapq.heappush(minheap, (nei_dist, nei))

        return min_cost
                