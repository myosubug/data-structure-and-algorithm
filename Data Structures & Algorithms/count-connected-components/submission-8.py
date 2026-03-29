class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n

        parent = {}

        def find(x):
            if x != parent.get(x, x):
                parent[x] = find(parent[x])
            return parent.get(x, x)

        def union(x, y):
            parent[find(x)] = find(y)

        for u, v in edges:
            union(u, v)

        return len({find(x) for x in range(n)})