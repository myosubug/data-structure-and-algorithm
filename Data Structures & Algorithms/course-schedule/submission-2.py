class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[] for n in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj_list[src].append(dst)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        processed = 0
        while q:
            node = q.popleft()
            processed += 1
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return processed == numCourses