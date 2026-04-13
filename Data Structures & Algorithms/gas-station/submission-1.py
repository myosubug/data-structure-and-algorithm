class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(cost) > sum(gas):
            return -1
        
        if n == 1:
            return 0

        candidates = []

        for i in range(n):
            if gas[i] > cost[i]:
                candidates.append(i)

        for index in candidates:
            j = 0
            temp_tank = gas[index]
            while j < n:
                actual_index = (index+1) % n
                temp_tank = temp_tank + gas[actual_index] - cost[actual_index]
                j += 1
            if temp_tank >= 0:
                return index
        

        return -1