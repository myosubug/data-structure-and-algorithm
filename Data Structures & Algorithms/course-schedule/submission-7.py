class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        adj_list = [[] for i in range(numCourses)]
        sorted_courses = []


        for s, e in prerequisites:
            degree[e] += 1
            adj_list[s].append(e)

        queue = deque([])

        for j, d in enumerate(degree):
            if d == 0:
                queue.append(j)

        while queue:
            popped = queue.popleft()
            sorted_courses.append(popped)
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)



        return True if len(sorted_courses) == numCourses else False