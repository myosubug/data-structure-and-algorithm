class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        


        degree = [0] * numCourses
        adj_list = [[] for n in range(numCourses)]

        for src, dst in prerequisites:
            degree[dst] += 1
            adj_list[src].append(dst)

        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)

        processed = 0

        while queue:
            popped = queue.popleft()
            processed += 1
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)

        return processed == numCourses