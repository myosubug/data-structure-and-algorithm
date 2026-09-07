class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_area = 0
        left, right = 0, len(h)-1

        while left < right:
            temp_area = (right-left) * min(h[left],h[right])
            max_area = max(max_area, temp_area)
            if h[left] > h[right]:
                right -= 1
            else:
                left += 1

        return max_area