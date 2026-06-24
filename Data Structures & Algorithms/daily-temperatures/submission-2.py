class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            for j in range(i+1, len(temperatures)):
                if t >= temperatures[j]:
                    continue
                else:
                    ret[i] = j - i
                    break

        return ret