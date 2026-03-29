class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        queue = deque([])
        processed = 0

        for start, end in prerequisites:
            adj_list[start].append(end)
            degree[end] += 1

        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)

        while queue:
            popped = queue.popleft()
            processed += 1
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)

        return processed == numCourses

