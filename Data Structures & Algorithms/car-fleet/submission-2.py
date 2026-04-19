class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])

        pair.sort(reverse=True)

        for p, s in pair:
            stack.append((target-p) / s)
            #  If the car ahead takes the same or more time, then the car behind will catch it 
            # and they merge into one fleet.
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)
                