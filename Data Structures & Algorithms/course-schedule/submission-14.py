from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        adj_list = defaultdict(list)
        roots = deque()
        order = []


        for dst, src in prerequisites:
            adj_list[src].append(dst)
            degree[dst] += 1


        for i, d in enumerate(degree):
            if d == 0:
                roots.append(i)

        while roots:
            popped = roots.popleft()
            order.append(popped)
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    roots.append(nei)

        return len(order) == numCourses