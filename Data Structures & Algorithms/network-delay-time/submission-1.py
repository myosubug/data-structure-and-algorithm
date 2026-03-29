class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}
        visited = set()
        minheap = [(0,k)]
        for s, d, t in times:
            if s not in adj_list:
                adj_list[s] = []
            adj_list[s].append((d,t))
        
        t = 0
        while minheap:
            dt, dn = heapq.heappop(minheap)
            if dn in visited:
                continue
            visited.add(dn)
            t = dt
            for nei, dist in adj_list.get(dn, []):
                if nei not in visited:
                    heapq.heappush(minheap, (dt+dist, nei))
        
        return t if len(visited) == n else -1