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

        if self.rank[pu] > self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = pv
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        counter = size
        dsu = DSU(size)
        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1:
                    if dsu.union(i,j):
                        counter -= 1
        
        return counter


        