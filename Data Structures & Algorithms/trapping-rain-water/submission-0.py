class Solution:
    def trap(self, height: List[int]) -> int:
        ret = 0

        for i, h in enumerate(height):
            left_max = 0 if i == 0 else max(height[:i])
            right_max = 0 if i == len(height)-1 else max(height[i+1:])

            temp = min(left_max, right_max) - h
            if temp > 0:
                ret += temp


        return ret