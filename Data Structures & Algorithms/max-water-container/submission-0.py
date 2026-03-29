class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start from left end and right end
        # define left, right and initial area (distance * min (left or right))

        # calculate the distance * min (left or right)
        # if it's bigger than previous value, udpate
        # otherwise move left or right
           # if left < right:
           #  left += 1 because we would want the bigger value for maximizing the area
           # vice versa for right

        left, right = 0, len(heights) - 1
        prev = min(heights[left],heights[right]) * (right-left)

        while left < right:
            temp_area = min(heights[left],heights[right]) * (right-left)
            if temp_area > prev:
                prev = temp_area
            else:
                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -= 1

        return prev