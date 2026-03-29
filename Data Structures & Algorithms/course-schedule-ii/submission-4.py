class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        adj_list = [[] for i in range(numCourses)] 
        ret = []
        roots = deque()
        
        for src, dst in prerequisites:
            adj_list[dst].append(src)
            degree[src] += 1
        
        for i, d in enumerate(degree):
            if d == 0:
                roots.append(i)

        while roots:
            popped = roots.popleft()
            ret.append(popped)
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    roots.append(nei)


        return ret if len(ret) == numCourses else []