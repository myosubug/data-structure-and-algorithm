class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depth = [0] * (numCourses)
        adj_list = {}
        roots = deque()
        ret = []

        for src, dst in prerequisites:
            if src not in adj_list:
                adj_list[src] = [dst]
            else:
                adj_list[src].append(dst)

            depth[dst] += 1


        for i, c in enumerate(depth):
            if c == 0:
                roots.append(i)

        while roots:
            popped = roots.popleft()
            ret.append(popped)
            if popped in adj_list:
                for nei in adj_list[popped]:
                    depth[nei] -= 1
                    if depth[nei] == 0:
                        roots.append(nei)


        return len(ret) == numCourses
