class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_copy = cost
        cost_copy.append(0)
        # cost_copy.append(0) # Removed extra append to keep logic consistent with length
        
        for i in range(len(cost_copy)-3, -1, -1):
            one_jump = float('inf')
            two_jump = float('inf')
            if i + 1 < len(cost_copy):
                one_jump = cost_copy[i] + cost_copy[i+1]
            if i + 2 < len(cost_copy):
                two_jump = cost_copy[i] + cost_copy[i+2]
            cost_copy[i] = min(one_jump, two_jump)


        return min(cost_copy[0], cost_copy[1])