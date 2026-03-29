class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = -1

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                p_i, p_h = stack.pop()
                max_area = max(max_area, (i-p_i) * p_h)
                start = p_i
            stack.append((start, h))

        for s_i, s_h in stack:
            max_area = max(max_area, (len(heights)-s_i) * s_h)

        return max_area