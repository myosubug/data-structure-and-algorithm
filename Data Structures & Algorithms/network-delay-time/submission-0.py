class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}
        for u, v, w in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((v,w))

        minheap = [(0,k)]
        visited = set()
        t = 0

        while minheap:
            dt, dn = heapq.heappop(minheap)
            if dn in visited:
                continue
            visited.add(dn)
            t = dt

            for zn, zt in edges.get(dn,[]):
                if zn not in visited:
                    heapq.heappush(minheap, (dt+zt, zn))
        
        return t if len(visited) == n else -1