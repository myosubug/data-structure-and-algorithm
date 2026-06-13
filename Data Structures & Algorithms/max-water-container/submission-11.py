class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(h)-1

        while left < right:
            temp_area = min(h[left],h[right]) * (right - left)
            max_area = max(max_area, temp_area)
            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
        return max_area