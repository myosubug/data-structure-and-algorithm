class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        degree = [0] * numCourses
        roots = deque([])
        ret = []


        for dst, src in prerequisites:
            if src not in adj_list:
                adj_list[src] = []
            adj_list[src].append(dst)
            degree[dst] += 1


        for i, d in enumerate(degree):
            if d == 0:
                roots.append(i)

        while roots:
            popped = roots.popleft()
            ret.append(popped)
            for nei in adj_list.get(popped, []):
                degree[nei] -= 1
                if degree[nei] == 0:
                    roots.append(nei)

        return ret if len(ret) == numCourses else []