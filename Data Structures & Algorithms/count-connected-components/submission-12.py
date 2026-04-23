class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, node):
        cur = node
        while cur != self.parents[cur]:
            self.parents[cur] = self.parents[self.parents[cur]]
            cur = self.parents[cur]
        return cur
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        # the higher the value, the higher rank    
        if self.rank[pu] > self.rank[pv]:
            pu, pv = pv, pu
        
        self.rank[pu] += self.rank[pv]
        self.parents[pv] = pu

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)
        
        for u, v in edges:
            if dsu.union(u,v):
                res -= 1
        
        return res
