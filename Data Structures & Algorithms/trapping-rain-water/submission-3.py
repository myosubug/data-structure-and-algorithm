class Solution:
    def trap(self, height: List[int]) -> int:
        total_trapped = 0

        # for i in range(1, len(height)-1):
        #     left_max = max(height[:i])
        #     right_max = max(height[i+1:])
        #     temp_trapped = min(left_max, right_max) - height[i]
        #     if temp_trapped < 0:
        #         temp_trapped = 0
        #     total_trapped += temp_trapped

        # return total_trapped
        if len(height) < 3:
            return 0
        max_from_left = [0] * len(height)
        max_from_right = [0] * len(height)

        max_from_left[0] = 0
        max_from_left[1] = height[0]
        for i in range(2, len(height)):
            max_from_left[i] = max(max_from_left[i-1], height[i-1])

        max_from_right[-1] = 0
        max_from_right[-2] = height[-1]
        for j in range(len(height)-3, -1, -1):
            max_from_right[j] = max(max_from_right[j+1], height[j+1])

        for k in range(1, len(height)-1):
            temp_trapped = max(0, min(max_from_left[k],max_from_right[k])-height[k])
            total_trapped += temp_trapped

        return total_trapped