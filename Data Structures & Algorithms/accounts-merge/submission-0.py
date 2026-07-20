class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

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
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = pu
        else:            
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = pv

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    dsu.union(i, emailToAcc[e])
                else:
                     emailToAcc[e] = i
        
        emailgroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = dsu.find(i)
            emailgroup[leader].append(e)

        ret = []
        for i, e in emailgroup.items():
            name = accounts[i][0]
            ret.append([name] + sorted(e))


        return ret