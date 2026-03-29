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


        '''
        [(30, 0)]
[0, 0, 0, 0, 0, 0, 0]
[(38, 1)]
[1, 0, 0, 0, 0, 0, 0]
[(38, 1), (30, 2)]
[1, 0, 0, 0, 0, 0, 0]
[(38, 1), (36, 3)]
[1, 0, 1, 0, 0, 0, 0]
[(38, 1), (36, 3), (35, 4)]
[1, 0, 1, 0, 0, 0, 0]
[(40, 5)]
[1, 4, 1, 2, 1, 0, 0]
[(40, 5), (28, 6)]
[1, 4, 1, 2, 1, 0, 0]
'''