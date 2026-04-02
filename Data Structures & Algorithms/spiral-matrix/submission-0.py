class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])

        left, right = 0, col-1
        top, bottom = 0, row-1

        ret = []

        while left <= right and top <= bottom:
            # towards right
            for tr in range(left, right+1):
                ret.append(matrix[top][tr])
            top += 1
            # towards bottom
            for tb in range(top, bottom+1):
                ret.append(matrix[tb][right])
            right -= 1
            
            if not (left <= right and top <= bottom):
                break

            # towards left
            for tl in range(right, left-1, -1):
                ret.append(matrix[bottom][tl])
            bottom -= 1
            #towards top
            for tt in range(bottom, top-1, -1):
                ret.append(matrix[tt][left])
            left += 1

        return ret