class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n)]
        visited = set()

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        q = deque([(0, -1)])
        visited.add(0)

        while q:
            cur, par = q.popleft()
            for nei in adj_list[cur]:
                if nei == par:
                    continue
                if nei in visited:
                    return False
                q.append((nei, cur))
                visited.add(nei)

        return len(visited) == n