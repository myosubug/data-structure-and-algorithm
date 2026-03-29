class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        ret = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            while q:
                popped = q.popleft()
                visit.add(popped)
                for nei in adj[popped]:
                    if nei not in visit:
                        q.append(nei)

        for node in range(n):
            if node not in visit:
                bfs(node)
                ret += 1
        

        return ret
