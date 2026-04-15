class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        zero_positions = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
        
        for i, j in zero_positions:
            self.applyZeroes(i, j, r, c, matrix)

    def applyZeroes(self, x, y, r, c, matrix):
        rows = []
        cols = []

        for i in range(r):
            rows.append([i, y])
        
        for j in range(c):
            cols.append([x, j])

        for a, b in rows:
            matrix[a][b] = 0

        for a, b in cols:
            matrix[a][b] = 0