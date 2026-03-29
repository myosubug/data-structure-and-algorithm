class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n+1)

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            pu, pv = pv, pu
        self.rank[pu] += self.rank[pv]
        self.parent[pv] = pu
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        count_unique = set()
        for u, v in edges:
            count_unique.add(u)
            count_unique.add(v)
        dsu = DSU(len(count_unique))

        for u, v in edges:
            if dsu.union(u,v) == False:
                return [u,v]

        return []
