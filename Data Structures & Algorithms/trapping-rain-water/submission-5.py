class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ret = [0] * n
        
        max_from_left = [0] * n
        max_from_right = [0] * n
        max_from_left[0] = height[0]
        max_from_right[-1] = height[-1]

        for i in range(1, n):
            max_from_left[i] = max(max_from_left[i-1], height[i])

        for j in range(n-2, -1, -1):
            max_from_right[j] = max(max_from_right[j+1], height[j])

        for k in range(1, n-1):
            ret[k] = min(max_from_left[k],max_from_right[k]) - height[k]
            if ret[k] < 0:
                ret[k] = 0

        return sum(ret)
        