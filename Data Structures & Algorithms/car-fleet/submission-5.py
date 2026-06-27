class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []

        for i in range(len(position)):
            pair.append([position[i], speed[i]])

        pair.sort(reverse = True)

        for p, s in pair:
            time_taken_to_target = (target-p) / s
            stack.append(time_taken_to_target)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        
        return len(stack)