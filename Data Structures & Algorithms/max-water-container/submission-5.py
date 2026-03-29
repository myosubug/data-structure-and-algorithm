class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights)-1

        while l < r:
            temp_area = (r-l) * min(heights[r], heights[l])
            max_area = max(temp_area, max_area)
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1

        return max_area