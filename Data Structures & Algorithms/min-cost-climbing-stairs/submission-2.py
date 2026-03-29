class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_copy = cost.copy()
        cost_copy.append(0)
        # cost_copy.append(0) # Removed extra append to keep logic consistent with length

        for i in range(len(cost_copy)-3, -1, -1):
            cost_copy[i] += min(cost_copy[i+1], cost_copy[i+2])


        return min(cost_copy[0], cost_copy[1])