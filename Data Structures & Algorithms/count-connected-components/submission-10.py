class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        visited = [False] * n
        count = 0

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        for node in range(n):
            if visited[node] == False:
                self.bfs(node, visited, adj_list)
                count += 1

        return count
    
    def bfs(self, node, visited, adj_list):
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in adj_list[cur]:
                if visited[nei] == False:
                    visited[nei] = True
                    q.append(nei)

        
