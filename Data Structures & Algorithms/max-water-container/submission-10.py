class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1


        while left < right:
            temp_area = (right-left) * min(heights[left], heights[right])
            max_area = max(max_area, temp_area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_area