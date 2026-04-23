class DSU:
    def __init__(self, n):
        self.parent = [ i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        current = node
        while current != self.parent[current]:
            self.parent[current] = self.parent[self.parent[current]]
            current = self.parent[current]
        return current

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)

        
        for u, v in edges:
            if not dsu.union(u,v):
                return [u,v]
        
        return []
        