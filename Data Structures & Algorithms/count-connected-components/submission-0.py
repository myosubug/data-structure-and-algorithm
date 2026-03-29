class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                popped = q.popleft()
                for nei in adj[popped]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei) 


        ret = 0

        for node in range(n):
            if not visit[node]:
                bfs(node)
                ret += 1
        
        return ret