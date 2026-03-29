class Solution:
    def trap(self, height: List[int]) -> int:
        # total_trapped_water = 0
        # for i in range(1, len(height)-1):
        #     leftMax = max(height[:i])
        #     rightMax = max(height[i+1:])
        #     temp_water = min(leftMax,rightMax) - height[i]
        #     if temp_water >= 0:
        #         total_trapped_water += temp_water

        # return total_trapped_water

        total_trapped_water = 0
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        for i in range(1, len(height)-1):
            leftMax[i] = max(height[i-1], leftMax[i-1])

        for j in range(len(height)-2, 0, -1):
            rightMax[j] = max(height[j+1], rightMax[j+1])

        for k in range(1, len(height)-1):
            temp = min(leftMax[k],rightMax[k]) - height[k]
            if temp >= 0:
                total_trapped_water += temp

        return total_trapped_water

