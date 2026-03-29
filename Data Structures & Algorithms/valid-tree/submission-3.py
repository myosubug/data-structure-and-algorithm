class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        q = deque([(0,-1)])
        visited = set()
        visited.add(0)

        while q:
            current, parent = q.popleft()
            for nei in adj[current]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append((nei, current))
                visited.add(nei)

        return len(visited) == n