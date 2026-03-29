class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        adj_list = [[] for i in range(numCourses)]
        q = deque()
        processed = 0

        for src, dst in prerequisites:
            degree[dst] += 1
            adj_list[src].append(dst)

        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)


        while q:
            popped = q.popleft()
            processed += 1
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)

        return processed == numCourses