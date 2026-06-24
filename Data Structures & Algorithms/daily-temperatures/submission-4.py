class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                indx, temp = stack.pop()
                ret[indx] = i - indx
            stack.append((i, t))

        return ret