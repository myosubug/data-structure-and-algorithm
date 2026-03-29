class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        adj_list = [[] for i in range(numCourses)]
        ret = []

        for s, e in prerequisites:
            degree[e] += 1
            adj_list[s].append(e)

        queue = deque([])
        for j, d in enumerate(degree):
            if d == 0:
                queue.append(j)

        while queue:
            popped = queue.popleft()
            ret.append(popped)
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)

        
        return ret[::-1] if len(ret) == numCourses else []