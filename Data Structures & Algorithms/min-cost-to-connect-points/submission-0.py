class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        in_tree = [False] * n

        min_dist[0] = 0
        total_cost = 0

        for _ in range(n):
            curr = -1
            # pick cheapest to visit
            for j in range(n):
                if not in_tree[j] and (curr == -1 or min_dist[j] < min_dist[curr]):
                    curr = j

            # add to tree
            in_tree[curr] = True
            total_cost += min_dist[curr]

            # update min_dist for remaining

            for j in range(n):
                if not in_tree[j]:
                    dist = abs(points[curr][0]-points[j][0]) + abs(points[curr][1]-points[j][1])
                    min_dist[j] = min(min_dist[j], dist)

        return total_cost