class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        visit = set()
        q = deque([(0, -1)])

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit.add(0)
        while q:
            current, parent = q.popleft()
            for nei in adj_list[current]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                q.append((nei,current))
                visit.add(nei)
        
        return len(visit) == n
        
