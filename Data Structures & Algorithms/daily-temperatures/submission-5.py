class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, temp = stack.pop()
                ret[idx] = i - idx
            stack.append((i, t))

        return ret
