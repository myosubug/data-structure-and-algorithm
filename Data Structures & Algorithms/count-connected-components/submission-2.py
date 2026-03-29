class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        ret = 0
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            while q:
                current = q.popleft() 
                visited.add(current)
                for nei in adj[current]:
                    if nei not in visited:
                        q.append(nei)

        
        for i in range(n):
            if i not in visited:
                bfs(i)
                ret += 1

        return ret