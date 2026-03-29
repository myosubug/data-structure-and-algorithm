class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        order = []
        queue = deque([])

        for end, start in prerequisites:
            adj_list[start].append(end)
            degree[end] += 1

        for i, n in enumerate(degree):
            if n == 0:
                queue.append(i)
        
        while queue:
            popped = queue.popleft()
            order.append(popped)
            for nei in adj_list[popped]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)
        
        return order if len(order) == numCourses else []