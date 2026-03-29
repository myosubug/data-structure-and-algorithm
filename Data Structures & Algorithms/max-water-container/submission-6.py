class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = float('-inf')

        l, r = 0, len(heights)-1

        while l < r:
            temp_area = (r-l) * min(heights[l], heights[r])
            ret = max(temp_area, ret)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return ret