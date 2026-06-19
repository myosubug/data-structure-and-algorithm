class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjacent_list = {}
        ret = []

        for dst, src in prerequisites:
            indegree[dst] += 1
            if src not in adjacent_list:
                adjacent_list[src] = []
            adjacent_list[src].append(dst)

        root = deque([])
        for i, n in enumerate(indegree):
            if n == 0:
                root.append(i)

        while root:
            popped = root.popleft()
            ret.append(popped)
            for nei in adjacent_list.get(popped, []):
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    root.append(nei)

        return ret if len(ret) == numCourses else []