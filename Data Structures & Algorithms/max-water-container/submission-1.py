class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        left = 0
        right = len(heights) - 1


        while left < right:
            smaller_side = min(heights[left], heights[right])
            max_area = max(max_area, smaller_side * (right - left))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area