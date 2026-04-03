class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # src -> dst
        # dst += 1
        # srd = [dst1, dst2, ...]

        adj_list = {}
        degree = [0] * numCourses
        root = deque([])
        ret = []

        for dst, src in prerequisites:
            degree[dst] += 1
            if src not in adj_list:
                adj_list[src] = []
            adj_list[src].append(dst)

        for i, n in enumerate(degree):
            if n == 0:
                root.append(i)


        while root:
            popped = root.popleft()
            ret.append(popped)
            for nei in adj_list.get(popped, []):
                degree[nei] -= 1
                if degree[nei] == 0:
                    root.append(nei)

        return True if len(ret) == numCourses else False
        