class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

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

        # the higher the rank, the more parent the node
        if self.rank[pu] > self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = self.parent[pu]
        else:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = self.parent[pv]

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                count += 1

        return n - count

        