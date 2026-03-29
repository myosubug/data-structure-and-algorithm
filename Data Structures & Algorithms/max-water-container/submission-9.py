class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights)-1

        while left < right:
            temp_area = (right-left) * min(heights[left],heights[right])
            max_area = max(max_area,temp_area)
            if heights[left]< heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area