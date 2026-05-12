class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj_list = {}

        for i, j in edges:
            if i not in adj_list:
                adj_list[i] = []
            if j not in adj_list:
                adj_list[j] = []
            adj_list[i].append(j)
            adj_list[j].append(i)

        queue = deque([(0, -1)])
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for nei in adj_list.get(node, []):
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                queue.append((nei, node))
                visited.add(nei)

        return len(visited) == n