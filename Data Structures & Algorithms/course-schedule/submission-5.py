class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        n = numCourses
        degree = [0] * n
        adj = [[] for i in range(n)]
        queue = deque([])
        processed = 0

        for src, dst in prerequisites:
            degree[dst] += 1
            adj[src].append(dst) 


        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)

        while queue:
            popped = queue.popleft()
            processed += 1
            for nei in adj[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)
        
        return processed == n