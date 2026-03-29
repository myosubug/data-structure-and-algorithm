class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temp)

        for i, t in enumerate(temp):
            while stack and stack[-1][0] < t:
                te, idx = stack.pop()
                ret[idx] = i-idx
            stack.append((t,i))

        return ret