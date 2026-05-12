class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbors = {}
        roots = deque()

        for end, start in prerequisites:
            indegree[end] += 1
            if start not in neighbors:
                neighbors[start] = []
            neighbors[start].append(end)
        

        for i, n in enumerate(indegree):
            if n == 0:
                roots.append(i)

        visited = 0

        while roots:
            popped = roots.popleft()
            visited += 1
            for nei in neighbors.get(popped, []):
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    roots.append(nei)


        return visited == numCourses
