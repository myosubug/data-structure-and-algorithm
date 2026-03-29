class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(0, -1)])
        visited.add(0)

        while q:
            cur, par = q.popleft()
            for nei in adj[cur]:
                if nei == par:
                    continue
                if nei in visited:
                    return False
                q.append((nei, cur))
                visited.add(nei)

        return len(visited) == n